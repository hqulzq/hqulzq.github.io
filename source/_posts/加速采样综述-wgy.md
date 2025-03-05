---
title: 加速采样综述-wgy
date: 2025-02-27 20:38:44
mathjax: true
tags:
  - diffusion
  - 论文 
categories:
  - AI
---

# Accelerated Sampling for Diffusion Models: A Survey

## 全文翻译

### 摘要
自2020年以来，扩散概率模型（DPMs）因其简单直接的优化过程，在图像生成领域取得了革命性进展。这些模型已广泛应用于图像、文本、语音等多个领域的各种任务中。然而，与生成对抗网络（GANs）等一步生成方法相比，扩散模型的多步迭代采样过程显著降低了其采样效率。为解决扩散模型采样过程中迭代次数多、速度慢的问题，研究人员开展了大量工作，并针对这些模型的特点取得了许多突破。本文首先概述了扩散模型的基本原理和框架，随后将扩散模型的加速采样技术分为三类：采样器设计、知识蒸馏和其他加速方法。接着，我们详细讨论了每类加速方法的主要特点、适用场景，以及它们的优缺点。最后，本文总结了扩散模型加速采样的研究进展，并探讨了该领域面临的关键挑战和未来潜在的研究方向。
<!-- more -->
### 引言
自2014年变分自编码器贝叶斯（VAEs）和2015年生成对抗网络（GANs）提出以来，深度学习生成模型已成为生成建模领域的重要驱动力。它们对图像生成与处理、三维重建，以及文本和语音生成等多个领域产生了深远影响。从生成模型的角度来看，目标是训练一个模型，记为$x \sim p_{\theta}(x | z)$，使得从任何先验分布$z \sim p(z)$中抽取一个样本$z$时，生成的样本$x$符合训练数据分布$x \sim p(x)$。在过去五年中，GANs和VAEs主导了深度生成模型领域，但GANs依赖对抗训练目标，常常出现模式崩溃和样本多样性有限的问题。另一方面，VAEs依赖替代目标（$(ELBO)$）来近似最大似然训练，这与目标分布的概率密度函数不具有渐近一致性，生成的图像往往比较模糊。然而，自2020年去噪扩散概率模型（DDPMs）问世以来，在深度生成模型领域，扩散模型占据了主导地位。其优化目标仅仅是最小化神经网络输出与噪声之间的L2范数，优化过程相对简单直接，样本质量也显著提高。因此，扩散模型范式的成功引领了深度生成模型的发展，使其成为当前的研究焦点。

然而，扩散模型通常构建为一个千步的马尔可夫过程，即先向图像中添加噪声，将其扩散到标准高斯噪声状态，然后使用神经网络学习噪声分布，从而逆向恢复图像。显然，这个马尔可夫链在采样过程中需要调用神经网络上千次，显著降低了模型的采样效率。因此，与GANs和VAEs等一步生成模型相比，DPMs的采样效率一直是其主要缺点，也是其应用于下游任务的重大障碍。针对这一问题，研究人员深入研究了扩散模型的原理，在提高其采样效率方面取得了显著进展。本文将现有的扩散模型加速采样技术分为三大类：第一类是基于使用常微分方程（ODE）或随机微分方程（SDE）设计高效采样器的策略，这类方法通常无需额外训练，能够用更少的采样步骤生成高质量样本；第二类是基于知识蒸馏的加速策略，一般需要在已有的预训练扩散模型上进行额外训练，其优势在于能够实现少步甚至一步采样；最后一类包括针对扩散模型特点设计的其他加速算法，例如增强转移概率$p(x_{t - 1} | x_{t})$的表达能力以挖掘扩散模型的潜力，以及通过搜索算法减少时间步长和网络结构的正交加速算法。这些方法通常不需要额外训练，并且与其他加速采样策略正交，进一步提高了采样速度。

本文主要分为两个部分：第一部分详细介绍扩散模型的基本原理，包括从离散视角出发的DDPMs（变分视角）和NCSNs（分数视角），以及从连续视角出发的ScoreSDE（分数视角）；第二部分系统回顾了三类扩散模型加速采样算法，深入讨论每种算法的特点、优缺点，并总结这些加速采样方法的研究进展。此外，我们还将探讨未来的研究挑战和潜在方向，为扩散模型加速采样的发展提供深入思考。 
### 2. 扩散模型的原理
作为深度生成模型的一种范式，自2020年以来，扩散模型已在机器学习的各个领域得到了成功应用。由于建模视角的多样性，扩散模型主要分为变分视角和分数视角，其中分数视角又进一步细分为离散视角和连续视角。本节将对扩散模型中这三种主要的建模方法进行全面的理论概述。
#### 2.1 去噪扩散概率模型（DDPMs）

DDPMs从变分视角进行建模，属于扩散模型的离散视角。它们主要由两个过程组成，即正向（扩散）过程和反向（逆扩散）过程。

- **正向过程**：DDPMs将正向过程定义为一个马尔可夫链，向原始数据分布$x_{0} \sim p(x_{0})$中添加噪声，直到$x_{t}$变为符合标准高斯分布的先验分布，即$x_{T} \sim N(0, I)$ 。该马尔可夫链的形式为$p(x_{1}, ..., x_{T} | x_{0})=\prod_{t = 1}^{T} p(x_{t} | x_{t - 1})$，其中在每个时间步$t$的扰动过程$p(x_{t} | x_{t - 1})$定义如下：
$$p\left(x_{t} | x_{t - 1}\right)=\mathcal{N}\left(x_{t} ; \sqrt{1-\beta_{t}} x_{t - 1}, \beta_{t} I\right), (1)$$
其中${\beta_{t} \in[0,1)}_{t = 1}^{T}$是在每个时间步$t$指定的常数，$I$表示单位矩阵，$\mathcal{N}$表示高斯分布。利用重参数化技巧，公式（1）可以转换为$x_{t}=\sqrt{1-\beta_{t}} x_{t - 1}+\sqrt{\beta_{t}} z$，其中$z \sim N(0, I)$。通过定义$\alpha = 1 - \beta$和$\bar{\alpha}_{t}=\prod_{i = 1}^{T} \alpha_{i}$，经过推导，$x_{t}$可以直接从$x_{0}$得到，如下所示：
$$x_{t}=\sqrt{\overline{\alpha}_{t}} x_{0}+\sqrt{1-\overline{\alpha}_{t}} z . (2)$$
- **反向过程**：由于正向过程被定义为每个时间步都遵循高斯分布的马尔可夫链，可以证明反向过程也是一个符合高斯分布的马尔可夫链。其形式为$p_{\theta}(x_{0}, ..., x_{T - 1} | x_{T})=\prod_{t = 1}^{T} p_{\theta}(x_{t - 1} | x_{t})$，$p_{latent }(x_{T})=N(0, I)$，其中每个时间步$t$的高斯分布参数化如下：
$$p_{\theta}\left(x_{t - 1} | x_{t}\right)=\mathcal{N}\left(x_{t - 1} ; \mu_{\theta}\left(x_{t}, t\right), \sigma_{\theta}\left(x_{t}, t\right)^{2} I\right), (3)$$
其中，$\mu_{\theta}(x_{t}, t)$和$\sigma_{\theta}(x_{t}, t)^{2}$分别表示高斯分布的均值和方差。为了训练反向过程的均值和方差，DDPMs使用最大似然估计推导出变分下界（$(ELBO)$），如下所示：
$$\begin{aligned} \log p_{\theta}\left(x_{0}\right) & \geq \log p_{\theta}\left(x_{0}\right)-D_{K L}\left(p\left(x_{1: T} | x_{0}\right)|| p_{\theta}\left(x_{1: T} | x_{0}\right)\right) \\ & =-\mathbb{E}_{p}\left[\log \frac{p\left(x_{1: T} | x_{0}\right)}{p_{\theta}\left(x_{n: T}\right)}\right] \\ & =E L B O, \end{aligned}$$
其中$D_{K L}(q, p)$表示分布$q$和$p$之间的库尔贝克 - 莱布勒散度（Kullback-Leibler divergence）。通过优化$ELBO$来训练模型参数，经过推导和简化后的损失函数如下：
$$L_{simple }=\mathbb{E}_{t, x_{0}, z}\left[\left\| z-z_{\theta}\left(x_{t}\left(x_{0}, z\right), t\right)\right\| ^{2}\right], (5)$$
其中$z_{\theta}$代表待训练的神经网络，$z \sim N(0, I)$。模型训练完成后，可以通过公式变换得到均值$\mu_{\theta}(x_{t}, t)$。为了简化，DDPMs将方差$\sigma_{\theta}(x_{t}, t)^{2}$定义为常数$\beta_{t}$或$\tilde{\beta}_{t}=\frac{1-\bar{\alpha}_{t - 1}}{1-\bar{\alpha}_{t}} \beta_{t}$ 。得到均值和方差后，就可以使用反向过程对$x_{0} \sim p(x_{0})$进行采样。

#### 2.2 噪声条件分数网络（NCSNs）
NCSNs定义了分数$\nabla_{x} \log p(x)$，并从分数建模的角度成功解决了生成模型面临的一系列设计挑战，包括对抗训练和结构约束。与DDPMs一样，NCSNs也属于扩散模型的离散视角。具体来说，NCSNs使用神经网络$s_{\theta}(x)$来近似分数$\nabla_{x}\log p(x)$，并基于这些训练好的神经网络，使用朗之万动力学采样（Langevin dynamics sampling）从训练数据分布中获取样本，如下所示：
$$x_{i + 1}=x_{i}+\epsilon \nabla_{x} \log p(x)+\sqrt{2 \epsilon} z_{i}, i = 0,1, ..., K, \quad(6)$$
其中$z_{i} \sim N(0, I)$，$x_{0} \sim \pi(x)$（$\pi(x)$是任意先验分布）；$\epsilon$代表步长，当$\epsilon \to 0$，$K \to \infty$时，$x_{K}$收敛到分布$p(x)$。根据上述描述，分数网络的训练目标如下：
$$\mathbb{E}_{p(x)}\left[\left\| \nabla_{x} \log p(x)-s_{\theta}(x)\right\| _{2}^{2}\right] .$$
由上述公式推导得到的最终优化目标包括$\text{tr}(\nabla_{x}^{2} \log p_{\theta}(x))$ 。然而，对于高维数据和深度神经网络，$\text{tr}(\nabla_{x}^{2} \log p_{\theta}(x))$的计算不具备可扩展性。为了解决这个问题，NCSNs从去噪分数匹配（Denoising Score Matching，DSM）中获得灵感，对原始训练数据分布引入多尺度噪声扰动。它们估计不同尺度下被扰动数据的分数，以逐步重构训练数据分布。NCSNs的优化目标如下：
$$\sum_{i = 1}^{L} \gamma(i) \mathbb{E}_{p_{\sigma_{i}}(x)}\left[\left\| \nabla_{x} \log p_{\sigma_{i}}(x)-s_{\theta}(x, i)\right\| _{2}^{2}\right], (8)$$
其中$\gamma(i)$是一个正加权函数，通常选择$\gamma(i)=\sigma_{i}^{2}$以满足$\gamma(i) \cdot(\nabla_{x} \log p_{\sigma_{i}}(x))^{2} \propto 1$。$\nabla_{x} \log p_{\sigma_{i}}(x)$可以展开并求解，结果为$-\frac{z}{\sigma_{i}}$，$z \sim N(0, I)$。利用训练好的分数网络，它们在每个噪声尺度上使用朗之万动力学采样，逐步从训练数据分布中获得样本$x_{0} \sim p(x_{0})$（退火朗之万动力学采样）。
#### 2.3 基于分数的随机微分方程（ScoreSDEs）
ScoreSDEs与NCSNs在建模方法上有共同之处，都基于分数视角。此外，ScoreSDEs通过随机微分方程（SDE）将扩散模型从离散视角扩展到连续视角，并证明了DDPMs和NCSNs是ScoreSDEs的特殊离散形式。
ScoreSDEs使用SDE对扩散过程进行建模，其方法与DDPMs和NCSNs类似。首先指定正向扩散过程，正向SDE定义如下：
$$d x=f(x, t) d t+g(t) d w, (9)$$
其中$f(x, t)$是一个向量值函数，称为$x(t)$的漂移系数；$g(t)$是一个实值函数，称为$x(t)$的扩散系数；$w$代表标准布朗运动。对应于正向SDE，可以推导出一个反向SDE，如下所示：
$$d x=\left[f(x, t)-g^{2}(t) \nabla_{x} \log p_{t}(x)\right] d t+g(t) d w, \quad(10)$$
其中$f(x, t)$、$g(t)$和$w$与正向SDE一致。此外，反向SDE包含一个未知项$\nabla_{x} \log p(x)$，可以观察到它对应于训练数据分布的分数。与NCSNs中使用的优化方法类似，这个未知项由一个经过优化的神经网络代替，从而得到反向SDE的解。通过反向SDE，可以使用许多采样算法从训练数据分布中获取样本，表示为$x_{0} \sim p(x_{0})$。例如，欧拉 - 丸山采样方法（Euler-Maruyama sampling method）如下所示：
$$\Delta x \leftarrow\left[f(x, t)-g^{2}(t) s_{\theta}(x, t)\right] \Delta t+g(t) \sqrt{|\Delta t|} z_{t}, \quad(11)$$
其中$z_{t} \sim N(0, I)$。使用上述SDE，也可以推导出一个常微分方程（ODE），得到与SDE一致的采样分布。该ODE表示如下：
$$d x=\left[f(x, t)-\frac{1}{2} g^{2}(t) \nabla_{x} \log p_{t}(x)\right] d t . (12)$$
最后，DDPMs和NCSNs可以统一为ScoreSDEs的特殊离散形式。与DDPMs对应的SDE是$d x=-\frac{1}{2} \beta_{t} x d t+\sqrt{\beta_{t}} d w$，与NCSNs对应的SDE是$d x=\sqrt{\frac{d \sigma_{i}^{2}}{d t}} d w$。 
### 3. 采样中的优化技术
为解决扩散模型在采样过程中因自回归多步迭代导致的采样效率低下问题，众多研究人员利用扩散模型的特性，提出了一系列改进的采样策略以加速采样过程。这些改进方法主要可分为三类：基于随机微分方程/常微分方程（SDE/ODE）设计高效采样器、基于知识蒸馏的加速策略，以及其他加速采样策略。本章将详细介绍这三类加速采样方法，旨在帮助读者全面了解当前加速采样技术的研究进展。
#### 3.1 高效SDE/ODE求解器设计
设计高效SDE/ODE求解器的目的是减少DDPMs、NCSNs和ScoreSDE采样算法所需的数千次采样迭代，同时确保边际分布$x_0 \sim p(x_0)$不变，从而使采样器能在更少的步骤内收敛。在采样过程中，SDE通过添加噪声引入随机性，通常可提高样本质量；而ODE由于缺少随机项，能实现更快的收敛。因此，加速采样求解器通常基于ODE进行设计。去噪扩散隐式模型（DDIM）是高效ODE求解器设计中的一个里程碑，它将采样过程中的数千步减少到不超过50步；DPM-Solver和DPM-Solver++比DDIM更快，得到了广泛认可。研究人员还证明了DDIM是其方法的一个特殊情况，进一步将采样收敛过程减少到约10步；AMED-Solver在设计高效ODE求解器的基础上，融入了极小的知识蒸馏成本，将采样步骤减少到约5步。本节将详细介绍上述四种高效ODE/SDE求解器设计算法。
##### 3.1.1 去噪扩散隐式模型
DDIM有两大主要贡献。第一，它提出可以从时间步$[1, ..., T]$的子序列构建一个长度为S的新正向子状态序列$\{x_{\tau_1}, ..., x_{\tau_S}\}$ ，通过反转这个子状态序列，能在更少的时间步内完成采样。观察DDPM的训练目标（公式5），可以明显看出，只要DDPM指定的分布$p(x_t | x_0)$不变，使用子状态序列的训练目标仍是原始训练目标的一个子集。这意味着现有的预训练DDPM模型可以利用该子序列进行采样。然而，DDIM的实验结果表明，采样使用的步数越少，样本质量越差，尤其是当DDPM子序列减少到100步以下时，样本质量会显著下降。

DDIM的第二个贡献是对DDPM的训练损失函数和采样过程进行了重新评估。从公式（5）可以看出，损失函数仅取决于分布$p(x_t | x_0)$，而不取决于马尔可夫链$p(x_t | x_{t - 1})$。这意味着DDPM的正向过程可以有多种定义方式，不一定局限于马尔可夫过程，只要保证每个时间步的边际分布不变，就能保留原始的扩散特性。这一发现促使了采样公式的新推导。DDPM表明其优化目标（公式（5）的训练过程）是最小化$D_{KL}(p(x_{t - 1} | x_t, x_0) \| p_{\theta}(x_{t - 1} | x_t))$ ，这意味着采样过程仅取决于$p(x_{t - 1} | x_t, x_0)$，利用贝叶斯定理可将其展开如下：
$$p\left(x_{t - 1} | x_{t}, x_{0}\right)=p\left(x_{t} | x_{t - 1}, x_{0}\right) \frac{p\left(x_{t - 1} | x_{0}\right)}{p\left(x_{t} | x_{0}\right)}, (13)$$

DDPM通过马尔可夫假设，设$p(x_t | x_{t - 1}, x_0) = p(x_t | x_{t - 1})$来解析求解公式（13）。然而，DDIM打破了DDPM的马尔可夫假设，提出由于训练过程与$p(x_t | x_{t - 1})$无关，采样过程可以重新定义以满足以下等式：
$$\int p\left(x_{t - 1} | x_{t}, x_{0}\right) p\left(x_{t} | x_{0}\right) d x_{t}=p\left(x_{t - 1} | x_{0}\right), \quad(14)$$

为了复用DDPM的预训练模型，DDIM使用待定系数法并结合公式（2）推导得到的采样过程如下：
$$\begin{aligned} x_{t - 1}= & \sqrt{\overline{\alpha}_{t - 1}}\left(\frac{x_{t}-\sqrt{1-\overline{\alpha}_{t}} z_{\theta}\left(x_{t}, t\right)}{\sqrt{\overline{\alpha}_{t}}}\right)+ \sqrt{1-\overline{\alpha}_{t - 1}-\sigma_{t}^{2}} z_{\theta}\left(x_{t}, t\right)+\sigma_{t} z_{t}, \end{aligned}$$
其中$z_t \sim N(0, I)$，$\sigma_{t}^{2}=\rho^{2} \tilde{\beta}_{t}$，$\rho \in[0,1]$。特别地，DDIM通过令$\sigma_t = 0$ ，将采样过程转化为ODE的离散形式。通过这种方式，与DDPM相比，DDIM能在不超过50步内实现高质量采样。
##### 3.1.2 DPM-Solver和DPM-Solver++
DPM-Solver深入分析了ScoreSDE中提出的ODE结构，发现其具有半线性特征。通过尽可能地解析求解该ODE，在少步采样方面取得了显著进展。最初，基于公式（8），梯度$\nabla_x \log p_{\sigma_i}(x)$的计算结果为$-\frac{z}{\sigma_i}$ ，这与公式（5）中DDPM的损失形式（即噪声差的平方欧几里得范数）一致。公式（12）中的ODE被重新定义如下：
$$\frac{d x_{t}}{ d t}=f(t) x_{t}+\frac{g^{2}(t)}{2 \sigma_{t}} \epsilon_{\theta}\left(x_{t}, t\right) .$$

在采样时，通常使用一阶欧拉 - 丸山方法（如公式（11）所示），或者使用类似龙格 - 库塔（Runge-Kutta）的高阶ODE求解器进一步求解该ODE。ODE的解通常表示为：
$$\begin{aligned} x_{t} & =\int_{T}^{t} \frac{d x_{t}}{d t}=\int_{T}^{s} \frac{d x_{t}}{d t}+\int_{s}^{t} \frac{d x_{t}}{d t} \\ & =x_{s}+\int_{s}^{t}\left(f(\tau) x_{\tau}+\frac{g^{2}(\tau)}{2 \sigma_{\tau}} \epsilon_{\theta}\left(x_{\tau}, \tau\right)\right) d \tau . \quad(17) \end{aligned}$$

然而，DPM-Solver指出，将ODE视为黑箱并直接应用高阶方法可能会忽略一些已知的ODE信息，导致结果不稳定，在少步采样中的性能不佳。因此，从ODE的半线性特征出发（$f(t)x_t$为线性部分，$\frac{g^{2}(t)}{2 \sigma_{t}} \epsilon_{\theta}(x_{t}, t)$为非线性部分），精确求解线性部分，并使用常数变易法进一步展开半线性ODE：
$$x_{t}=e^{\int_{s}^{t} f(\tau) d \tau} x_{s}+\int_{s}^{t}\left(e^{\int_{\tau}^{t} f(r) d r} \frac{g^{2}(\tau)}{2 \sigma_{\tau}} \epsilon_{\theta}\left(x_{\tau}, \tau\right)\right) d \tau .$$
与公式（17）相比，公式（18）精确计算了ODE的线性部分$e^{\int_{s}^{t} f(\tau) d \tau} x_{s}$。此外，通过代入$\lambda_{t}:=\log (\alpha_{t} / \sigma_{t})$（对数信噪比的一半），ODE求解器被简化为：
$$x_{t}=\frac{\alpha_{t}}{\alpha_{s}} x_{s}-\alpha_{t} \int_{\lambda_{s}}^{\lambda_{t}} e^{-\lambda} \hat{\epsilon}_{\theta}\left(\hat{x}_{\lambda}, \lambda\right) d \lambda . (19)$$

公式（19）表示DPM-Solver对半线性ODE的解。通过在$\lambda_{t_{i - 1}}$处对$\hat{\epsilon}_{\theta}(\hat{x}_{\lambda}, \lambda)$进行泰勒展开，可以得到不同阶数的ODE近似值，如下所示：
$$\begin{aligned} x_{t_{i - 1} \to t_{i}}= & \frac{\alpha_{t_{i}}}{\alpha_{t_{i - 1}}} \tilde{x}_{t_{i - 1}}-\alpha_{t_{i}} \sum_{n = 0}^{k - 1} \hat{\epsilon}_{\theta}^{(n)}\left(\hat{x}_{\lambda_{t_{i - 1}}}, \lambda_{t_{i - 1}}\right) \\ & \times \int_{\lambda_{t_{i - 1}}}^{\lambda_{t_{i}}} e^{-\lambda} \frac{\left(\lambda-\lambda_{t_{i - 1}}\right)^{n}}{n!} d \lambda+\mathcal{O}\left(h_{i}^{k + 1}\right) . \\ & \times(20) \end{aligned}$$

DPM-Solver的另一个关键贡献是发现公式（20）中的积分$\int e^{-\lambda} \frac{(\lambda-\lambda_{t_{i - 1}})^{n}}{n!} d \lambda$可以通过分部积分法解析求解，进一步优化ODE的解，得到最终的采样算法（$k = 1$时）：
$$x_{t_{i - 1} \to t_{i}}=\frac{\alpha_{t_{i}}}{\alpha_{t_{i - 1}}} \tilde{x}_{t_{i - 1}}-\sigma_{t_{i}}\left(e^{h_{i}} - 1\right) \epsilon_{\theta}\left(\tilde{x}_{t_{i - 1}}, t_{i - 1}\right)+\mathcal{O}\left(h_{i}^{2}\right),$$
其中$h_{i}=\lambda_{t_{i}}-\lambda_{t_{i - 1}}$ 。通过选择不同的$k$值，可以得到不同阶数的$DPM-Solver - k$ 。值得注意的是，当$k = 1$时，ODE的解与DDIM一致，这解释了为什么DDIM在少步采样中表现良好，因为它考虑了ODE的半线性性质。采用更高阶的解（$k = 2,3$ ），DPM-Solver在少步采样场景中取得了优于DDIM的结果，将1000步的马尔可夫链迭代压缩到大约10步。

在DPM-Solver++的研究中发现，与DPM-Solver和PNDM等高阶ODE求解方法相比，当应用于条件扩散模型（如图文生成任务）的少步采样时，这些高阶方法的采样结果不如一阶的DDIM方法有效。因此，DPM-Solver++对条件扩散模型中DPM-Solver的采样过程进行了一些调整。首先，通过观察条件扩散模型的原理，包括分类器引导采样，有：
$$\tilde{\epsilon}_{\theta}\left(x_{t}, t, c\right):=\epsilon_{\theta}\left(x_{t}, t\right)-s \cdot \sigma_{t} \nabla_{x_{t}} \log p_{\phi}\left(c | x_{t}, t\right), \quad(22)$$
其中$s > 0$表示引导尺度。除了分类器引导生成算法，还有无分类器引导扩散算法，其原理描述如下：
$$\epsilon_{\theta}\left(x_{t}, t, c\right):=s \cdot \epsilon_{\theta}\left(x_{t}, t, c\right)+(1 - s) \cdot \epsilon_{\theta}\left(x_{t}, t, \varnothing\right) .(23)$$
观察公式（22）和（23），两者都涉及引导尺度$s$。DPM-Solver++的实验结果表明，引导尺度越大，采样质量越差。直观地说，较大的引导尺度会放大采样方程中模型输出的导数，使高阶ODE求解器对误差放大更加敏感，导致采样性能不如一阶的DDIM方法。此外，使用噪声网络$\epsilon_{\theta}$构建ODE无法将样本$x_{\theta}$的范围控制在$[-1, 1]$内，导致 “训练 - 测试不匹配” 问题。考虑到这些问题，DPM-Solver++从样本网络$x_{\theta}$的角度出发，使用重采样来替换$x_{\theta}:=$ $(x_{t}-\sigma_{t} \epsilon_{\theta}) / \alpha_{t}$ ，并重新推导DPM-Solver公式，得到新的采样方程如下：
$$x_{t}=\frac{\sigma_{t}}{\sigma_{s}} x_{s}+\sigma_{t} \int_{\lambda_{s}}^{\lambda_{t}} e^{\lambda} \hat{x}_{\theta}\left(\hat{x}_{\lambda}, \lambda\right) d \lambda, (24)$$
公式中的符号保持其先前定义的含义。基于此方法，DPM-Solver++使用泰勒展开尽可能地解析计算ODE，并选择二阶采样作为最佳平衡，因为高阶ODE会放大与引导尺度$s$相关的误差。为了与DPM-Solver进行比较，将DPM-Solver++的样本网络$x_{\theta}$替换为噪声网络$\epsilon_{\theta}$ 。DPM-Solver++噪声网络的具体二阶采样公式如下：
$$u_{i}=\frac{\alpha_{s_{i}}}{\alpha_{t_{i - 1}}} \overline{x}_{t_{i - 1}}-\sigma_{s_{i}}\left(e^{r_{i} h_{i}} - 1\right) \epsilon_{\theta}\left(\overline{x}_{t_{i - 1}}, t_{i - 1}\right)$$
$$\begin{aligned} \tilde{x}_{t_{i}} & =\frac{\alpha_{t_{i}}}{\alpha_{t_{i - 1}}} \tilde{x}_{t_{i - 1}}-\sigma_{t_{i}}\left(e^{h_{i}} - 1\right) \epsilon_{\theta}\left(\tilde{x}_{t_{i - 1}}, t_{i - 1}\right) \\ & -\frac{\sigma_{t_{i}}}{2 r_{i}}\left(e^{h_{i}} - 1\right) e^{-r_{i} h_{i}}\left(\epsilon_{\theta}\left(u_{i}, s_{i}\right)-\epsilon_{\theta}\left(\tilde{x}_{t_{i - 1}}, t_{i - 1}\right)\right) \end{aligned}$$
该公式中的符号与先前定义的含义相同。与DPM-Solver的唯一区别是，DPM-Solver++包含一个额外项$e^{-r_{i} h_{i}} < 1$，这有助于减少其后验误差项引入的误差。这也证明了从样本网络$x_{\theta}$的角度进行建模的优势。通过实验和理论分析，DPM-Solver++已被证明在条件扩散模型的少步采样中优于一阶的DDIM方法和其他二阶ODE采样算法。
##### 3.1.3 AMED-Solver
在AMED-Solver的研究中，它类比积分中值定理，以极小的蒸馏成本在大约5步内实现高质量采样。首先，定义一个扩散常微分方程（ODE）$\frac{dx_t}{dt}=\epsilon_{\theta}(x_t,t)$，根据基于分数的随机微分方程（ScoreSDE），其正向和反向ODE是一致的。对这个ODE进行积分，可得到精确的解析表达式：
$$x_{t_n}=x_{t_{n + 1}}+\int_{t_{n + 1}}^{t_n}\epsilon_{\theta}(x_t,t)dt \tag{26}$$
然后，类比积分中值定理，我们知道存在一点$s_n\in(t_n,t_{n + 1})$，使得以下等式成立：
$$\int_{t_n}^{t_{n + 1}}\epsilon_{\theta}(x_t,t)dt=\epsilon_{\theta}(x_{s_n},s_n)$$
然而，积分中值定理通常只适用于一维函数，对于向量函数一般并不成立。尽管如此，AMED-Solver通过主成分分析发现，这个ODE的采样轨迹在二维子空间内几乎落在一条直线上，这使得上述等式可以用积分中值定理来近似。因此，利用积分中值定理变换后的采样公式可近似为：
$$x_{t_n}\approx x_{t_{n + 1}}+(t_n - t_{n + 1})\epsilon_{\theta}(x_{s_n},s_n) \tag{28}$$
进一步地，当选择$s_n=\sqrt{t_nt_{n + 1}}$时，这个近似等式就转化为DPM-Solver - 2的采样策略。AMED-Solver并不满足于此，它使用欧拉 - 丸山方法来估计公式（28）中的$x_{s_n}$：
$$x_{s_n}=x_{t_{n + 1}}-\epsilon_{\theta}(x_{t_{n + 1}},t_{n + 1})(t_{n + 1}-s_n) \tag{29}$$
此时，唯一的未知参数是$s_n$，AMED-Solver通过知识蒸馏策略，用一个神经网络来近似它，表示为：
$$s_n = g_{\phi}(h_{t_{n + 1}},t_{n + 1}) \tag{30}$$
与蒸馏样本$x_{\theta}$相比，蒸馏$s_n$的成本极低，大大节省了蒸馏时间。通过这种策略，AMED-Solver能够以极小的训练成本完成几步内的高效采样。
AMED-Solver被视为一种求解器设计方法，而非蒸馏方法，因为它的蒸馏成本极小。模型蒸馏后，在采样时可以灵活选择步长，这与传统固定步长的蒸馏方法不同。与像DDIM和DPM-Solver这类无需训练的方法相比，AMED-Solver进一步减少了采样步骤。与完全基于知识蒸馏的算法相比，它仅需极小的训练成本。这种将两类加速采样算法相结合的方法，或许为未来的研究提供了一个更有效的方向。 

#### 3.2. 基于知识蒸馏的方法
基于知识蒸馏的方法主要通过现有的预训练扩散模型来指导训练，从而获得能够在更少步骤内采样出高质量样本的新模型。由于常微分方程（ODE）具有确定性解且不会引入随机噪声，知识蒸馏算法通常基于ODE进行训练。例如，渐进蒸馏（Progressive Distillation，PD）算法基于DDIM采样算法进行训练，在训练过程中以指数方式逐步减少采样步骤，能够在5步内实现高质量采样。另一个例子是一致性模型（Consistency Models，CM），它在现有预训练模型的基础上，提炼出能够进行一步采样的高效采样网络。基于知识蒸馏的加速采样算法可以最大程度地压缩采样步骤，获得高效的采样网络。然而，这种方法通常需要大量额外的训练资源，并且知识蒸馏算法往往难以应用于大型预训练模型，蒸馏后的网络可能会丢失许多中间步骤的信息。
##### 3.2.1 渐进蒸馏
PD算法类比标准扩散模型的训练步骤，融入了知识蒸馏算法。最初，PD将预测噪声$\hat{\epsilon}_{\theta}(z_{t})$修改为预测样本$\hat{x}_{\theta}(z_{t})$，因为在采样过程中，信噪比$\alpha_{t}^{2} / \sigma_{t}^{2}$会逐渐趋近于零。对于少步采样而言，将噪声网络转换为样本网络会导致更大的误差，如下所示：
$$x_{\theta}\left(z_{t}\right)=\frac{1}{\alpha_{t}}\left(z_{t}-\sigma_{t} \hat{\epsilon}_{\theta}\left(z_{t}\right)\right), \alpha_{t} \to 0. \tag{31}$$
选择样本网络作为蒸馏损失是大多数知识蒸馏算法的常见选择。随后，PD使用现有的预训练模型作为教师模型$\hat{x}_{\eta}(z_{t})$，并将学生模型$\hat{x}_{\theta}(z_{t})$初始化为教师模型。在每次渐进迭代中，教师模型通过两个DDIM采样步骤生成采样样本，如下所示：
$$\begin{cases}
z_{t'}=\alpha_{t'} \hat{x}_{\eta}\left(z_{t}\right)+\frac{\sigma_{t'}}{\sigma_{t}}\left(z_{t}-\alpha_{t} \hat{x}_{\eta}\left(z_{t}\right)\right) \\
z_{t''}=\alpha_{t''} \hat{x}_{\eta}\left(z_{t'}\right)+\frac{\sigma_{t''}}{\sigma_{t'}}\left(z_{t'}-\alpha_{t'} \hat{x}_{\eta}\left(z_{t'}\right)\right)
\end{cases}\tag{32}$$
其中$t' = t - 0.5 / N$，$t^{\prime \prime}=t - 1 / N$，$N$是当前阶段的总采样步数。然后，学生模型通过一个DDIM采样步骤获得与教师模型一致的采样样本。这可以通过反向使用DDIM采样公式来实现，进而得到学生模型的优化目标：
$$\tilde{x}=\frac{z_{t''}-\left(\sigma_{t''} / \sigma_{t}\right) z_{t}}{\alpha_{t''}-\left(\sigma_{t''} / \sigma_{t}\right) \alpha_{t}}. \tag{33}$$
最后，学生模型通过蒸馏损失函数使这两个采样样本对齐，从而进行优化：
$$L_{\theta}=w\left(\lambda_{t}\right)\left\|\tilde{x}-\hat{x}_{\theta}\left(z_{t}\right)\right\| _{2}^{2}. \tag{34}$$
每次迭代后，总采样步数减半，即$N = N / 2$，并将教师模型更新为当前阶段的学生模型。通过持续迭代，采样步骤可以以指数方式减少，从而获得一个步数更少的高效采样网络。
##### 3.2.2 一致性模型
CM算法是一种基于预训练扩散模型的蒸馏算法。通过蒸馏训练，CM能够实现单步高质量采样。最初，定义扩散ODE如下：
$$\frac{d x_{t}}{d t}=-t s_{\phi}\left(x_{t}, t\right). \tag{35}$$
对于给定的解轨迹$\{x_{t}\}_{t \in[\epsilon, T]}$，定义一个一致性函数$f: (x_{t}, t) \mapsto x_{\epsilon}$，该函数需要满足自一致性，即对于$t, t' \in[\epsilon, T]$，有$f(x_{t}, t)=f(x_{t'}, t')$。一致性函数的参数化形式为：
$$f_{\theta}(x, t)=c_{skip }(t) x+c_{out }(t) F_{\theta}(x, t), \tag{36}$$
其中$c_{skip }(t)$和$c_{out }(t)$是任意可微函数。基于一致性函数，CM的一致性蒸馏损失定义如下：
$$\mathcal{L}\left(\theta, \theta^{-} ; \phi\right) \leftarrow \lambda\left(t_{n}\right) d\left(f_{\theta}\left(x_{t_{n+1}}, t_{n+1}\right), f_{\theta^{-}}\left(\hat{x}_{t_{n}}^{\phi}, t_{n}\right)\right), \tag{37}$$
其中$\theta^{-}$表示指数移动平均（EMA）训练方法中前一阶段的参数，$\phi$表示预训练模型的参数。$\hat{x}_{t_{n}}^{\phi}$可以通过以下公式获得：
$$\hat{x}_{t_{n}}^{\phi}:=x_{t_{n+1}}+\left(t_{n}-t_{n+1}\right) \Phi\left(x_{t_{n+1}}, t_{n+1} ; \phi\right), \tag{38}$$
其中$\Phi(x_{t_{n+1}}, t_{n+1} ; \phi)$是一个数值ODE求解器。当选择一阶欧拉 - 丸山ODE求解器时，该公式简化为：
$$\hat{x}_{t_{n}}^{\phi}=x_{t_{n+1}}-\left(t_{n}-t_{n+1}\right) t_{n+1} s_{\phi}\left(x_{t_{n+1}}, t_{n+1}\right). \tag{39}$$
通过这些步骤进行蒸馏训练得到的新模型，能够实现单步高质量采样。 

#### 3.3. 其他加速采样策略
本章介绍了专门针对扩散模型特点设计的其他加速采样算法。这些算法可进一步分为两类：第一类是从独特视角设计的加速策略，与现有采样方法相互正交；第二类包括不属于上述加速采样算法类别的方法，例如，通过重新审视扩散模型并增强转移概率$p(x_{t - 1}|x_{t})$的表达能力，旨在深入挖掘扩散模型的潜力。
##### 3.3.1 正交加速采样算法
AutoDiffusion是一种正交加速算法，它观察到扩散模型采样过程中步长和模型结构存在冗余，并指出仅仅均匀减少时间步长并非最优的加速方法。因此，AutoDiffusion设定一个目标采样步长，并采用进化搜索算法，通过交叉和变异操作来寻找最优的采样步长序列和模型结构。尽管这种方法需要额外的搜索时间，但所需成本明显低于蒸馏的成本。此外，由于它与现有加速算法相互正交，因此可以在DDIM和DPM - Solver等方法的基础上进一步提高采样效率。

自适应动量采样器（Adaptive Momentum Sampler，AMS）方法注意到扩散模型的采样过程与随机梯度下降（Stochastic Gradient Descent，SGD）算法存在相似之处。因此，通过引入动量机制，它加速了扩散模型的采样过程。此外，通过采用Adam方法进行自适应动量采样，它进一步提高了采样效率。与AutoDiffusion一样，AMS与现有加速算法相互正交。调整动量积累参数可以在现有加速算法的基础上进一步提高采样效率，且无需额外训练。
##### 3.3.2 其他专门的加速采样设计
Analytic - DPM对扩散模型进行了深入分析，以增强转移概率$p(x_{t - 1}|x_{t})$的表达能力，从而释放扩散模型的潜力，实现以更少的步骤提高模型采样质量的目标。在DDIM中，通过打破马尔可夫链假设，获得了$p(x_{t - 1}|x_{t}, x_{0})$的解析表达式。利用$x_{0}=\frac{x_{t}-\sqrt{1-\bar{\alpha}_{t}}z_{\theta}}{\sqrt{\bar{\alpha}_{t}}}$，进一步推导出转移概率$p(x_{t - 1}|x_{t})$。然而，从贝叶斯的角度来看，将$x_{t}$转换为$x_{0}$的过程应包含一定程度的不确定性，不应由确定性函数来描述，而应由概率分布来表示。这个过程可以严格表示为：
$$p(x_{t - 1}|x_{t})=\int p(x_{t - 1}|x_{t}, x_{0})p(x_{0}|x_{t})dx_{0} \tag{40}$$
基于此，公式（40）中的分布$p(x_{0}|x_{t})$可以用正态分布$N(x_{0};\bar{\mu}(x_{t}), \bar{\sigma}_{t}^{2}I)$来近似。推导表明，均值的解析表达式保持不变，而方差的推导形式如下：
$$\overline{\sigma}_{t}^{2}=\frac{\overline{\beta}_{t}^{2}}{\overline{\alpha}_{t}^{2}}\left(1-\frac{1}{d}\mathbb{E}_{x_{t}\sim p(x_{t})}[\|\epsilon_{\theta}(x_{t}, t)\|^{2}]\right) \tag{41}$$
其中$d = dim(x)$。因此，我们得到了修正后的转移概率$p(x_{t - 1}|x_{t})$的解析形式，其中均值不变，通过将公式（41）代入公式（40）得到方差，进一步推导出最优方差$\sigma_{t}^{*2}$如下：
$$\begin{align*}
\sigma_{t}^{*2}&=\sigma_{t}^{2}+\left(\sqrt{\frac{\overline{\beta}_{t}}{\alpha_{t}}}-\sqrt{\overline{\beta}_{t - 1}-\sigma_{t}^{2}}\right)^{2}\\
&\times\left(1-\overline{\beta}_{t}\mathbb{E}_{x_{t}\sim p(x_{t})}\left[\frac{\|\nabla_{x_{t}}\log p_{t}(x_{t})\|^{2}}{d}\right]\right)
\end{align*} \tag{42}$$
其中符号保持其先前定义，$\sigma_{t}^{2}$是DDIM中一个可调整的方差超参数。有了最优均值和估计的最优方差，我们就得到了更准确的转移概率$p(x_{t - 1}|x_{t})$。Analytic - DPM通过实验验证，修正后的方差可以增强转移概率的表达能力，并在更少的步骤内进一步提高采样质量。尽管获得了转移概率的最优均值和方差的解析形式，但最优方差中的未知项$\mathbb{E}_{x_{t}\sim p(x_{t})}\|\nabla_{x_{t}}\log p_{t}(x_{t})\|^{2}$需要进行近似。此外，由于扩散模型原理在少步采样中存在固有局限性，以及训练损失未被最小化等问题，采样过程中可能会出现累积误差，这表明Analytic - DPM并非少步采样的绝对最优算法。

去噪扩散生成对抗网络（Denoising Diffusion Gans，DDG）通过整合生成对抗网络（GANs）的框架，显著增强了扩散模型中转移概率$p(x_{t - 1}|x_{t})$的表达能力。DDG的核心思想是解决传统扩散模型在增加扩散步骤时遇到的局限性，传统扩散模型通常假设转移概率服从高斯分布，而这一前提仅在$\beta_{t}$较小时成立。随着扩散步骤的增加，$\beta_{t}$的值增大，导致转移概率偏离高斯分布，使得训练目标不再适用。为了克服这个问题，DDG不再将转移概率限制为高斯分布，并重新定义了损失函数。最初，DDG引入了一个判别器损失函数，表示为：
$$\begin{align*}
&\min_{\phi}\sum_{t \geq 1}\mathbb{E}_{p(x_{t})}\left[\mathbb{E}_{p(x_{t - 1}|x_{t})}[- \log(D_{\phi}(x_{t - 1}, x_{t}, t))]\right.\\
&\left.+\mathbb{E}_{p_{\theta}(x_{t - 1}|x_{t})}[- \log(1 - D_{\phi}(x_{t - 1}, x_{t}, t))]\right]
\end{align*} \tag{43}$$
使用公式（43）进行优化，训练出一个判别器$D_{\phi}(x_{t - 1}, x_{t}, t))$，它能够区分来自生成器$p_{\theta}(x_{t - 1}|x_{t})$的样本和来自真实分布$p(x_{t - 1}|x_{t})$的样本。随后，定义一个用于训练生成器的损失函数如下：
$$\max_{\theta}\sum_{t \geq 1}\mathbb{E}_{p(x_{t})}\mathbb{E}_{p_{\theta}(x_{t - 1}|x_{t})}[\log(D_{\phi}(x_{t - 1}, x_{t}, t))] \tag{44}$$
使用公式（44）进行训练的目的是获得一个生成器$p_{\theta}(x_{t - 1}|x_{t})$，其生成的样本能让判别器$D_{\phi}(x_{t - 1}, x_{t}, t))$难以区分。通过这种交替训练机制，DDG能够有效缓解GANs训练过程中多样性不足和模式崩溃的问题，同时减少采样步骤。它还增强了扩散模型表达转移概率$p(x_{t - 1}|x_{t})$的能力，克服了对高斯分布的依赖，实现了少步高质量采样。 

### 4. 讨论
#### 4.1 加速采样算法总结
如前文所述，我们将扩散模型的加速采样算法主要分为三大类。在基于随机微分方程/常微分方程（SDE/ODE）设计高效采样器方面，我们探讨了去噪扩散隐式模型（DDIM）、DPM-Solver系列和AMED-Solver等算法的原理和特点；在基于知识蒸馏的加速采样算法方面，我们简要总结了渐进蒸馏（PD）和一致性模型（CM）算法的基本原理，并讨论了这类采样算法的优缺点；最后，我们详细介绍了其他加速采样算法，这些算法又细分为正交加速方法，包括自动扩散（AutoDiffusion）和自适应动量采样器（AMS），同时还深入讨论了未归类于上述类别的算法原理，如Analytic-DPM和去噪扩散生成对抗网络（DDG）算法。
#### 4.2 问题、挑战与未来方向
在基于SDE/ODE设计高效采样器的类别中，面临的主要问题是无法将采样步骤压缩到与生成对抗网络（GANs）和变分自编码器（VAEs）等一步生成模型相当的水平。继续深入研究扩散模型的基本原理和潜力，以及充分利用预训练模型的信息以进一步减少所需的采样步骤，仍然是该研究领域的关键目标。

对于基于知识蒸馏的加速算法，尽管它们能够实现扩散模型的一步采样，但这种方法难以直接应用于大型预训练模型，并且会导致中间步骤信息的丢失，通常还需要大量额外的训练成本。因此，如何降低蒸馏训练的成本，或者在采样步骤和训练成本之间找到平衡，是知识蒸馏类加速采样算法的一个研究方向。

其他加速采样算法，无论是正交加速方法、提升转移概率$p(x_{t - 1}|x_{t})$的表达能力的方法，还是从其他独特视角加速采样的方法，都在不同程度上为深入理解扩散模型提供了思路，且大多数方法不需要额外的训练成本。继续探索扩散模型的基本原理，以及如何有效地将这类算法与其他加速方法结合，以实现更高效的采样压缩，是该领域的一个重要研究目标。

最后，有效整合上述三类加速算法，平衡各种方法的优缺点，以设计高效的加速采样算法，也是一个重要的研究目标。例如，AMED-Solver通过其独特的采样器设计，利用极小的蒸馏成本实现了约5步的加速采样，就是一个很好的案例。此外，探索如何使用正交加速采样算法来降低蒸馏训练的成本，也将是一个有价值的研究方向。 

### 5. 结论
本文深入探讨了扩散模型的基本原理及其局限性，并全面回顾了加速扩散模型采样技术的最新进展。具体而言，我们详细讨论了从不同视角（包括DDPMs、NCSNs和ScoreSDE）对扩散模型原理的理解，强调了生成速度的限制是扩散模型发展的一个重大瓶颈。为了克服这一挑战，我们系统地分类和回顾了现有的加速扩散模型采样算法，这些算法主要分为三类：采样器设计、知识蒸馏技术和其他加速方法。我们不仅阐述了这些加速采样算法的基本原理，还分析了它们的优缺点以及适用场景。在文章的最后部分，我们讨论了加速采样领域面临的关键问题和挑战，并对未来的研究方向进行了展望。 