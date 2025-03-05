---
title: PFDDIFF论文精读
date: 2025-02-27 21:38:29
mathjax: true
tags:
  - diffusion
  - 论文 
categories:
  - AI
---

# PFDDIFF论文精读
## 全文翻译
### 摘要
扩散概率模型（Diffusion Probabilistic Models, DPMs）在图像生成领域展现出巨大潜力，但其采样效率受限于大量的去噪步骤。现有的解决方案大多通过提出快速常微分方程（ODE）求解器来加速采样过程。然而，当函数评估次数（NFE）较少时，ODE 求解器不可避免的离散化误差会被显著放大。在本研究中，我们提出了 PFDiff，这是一种全新的无需训练的正交跳步策略，它能使现有的快速 ODE 求解器在较少的 NFE 下运行。具体而言，PFDiff 首先利用过去时间步的分数替换来预测一个 “跳板” 状态。随后，它结合受 Nesterov 动量启发的前瞻更新机制，利用这个 “跳板” 状态快速更新当前的中间状态。这种方法在减少不必要的 NFE 的同时，还能校正一阶 ODE 求解器固有的离散化误差。实验结果表明，PFDiff 在各种预训练的 DPM 模型上都具有灵活的适用性，在条件 DPM 模型中表现尤为出色，超越了以往最先进的无需训练的方法。例如，以 DDIM 为基线，在 ImageNet 64x64 数据集上使用分类器引导时，我们的方法达到了 16.46 的 FID（4 次 NFE），而 DDIM 的 FID 为 138.81；在引导尺度为 7.5 的 Stable Diffusion 模型上，我们的方法以 10 次 NFE 达到了 13.06 的 FID。代码可在https://github.com/onefly123/PFDiff获取。
<!-- more -->
### 1. 引言
近年来，扩散概率模型（DPMs）（Sohl-Dickstein等人，2015；Ho等人，2020；Song等人，2020b）在包括图像生成（Dhariwal和Nichol，2021；Peebles和Xie，2023；Karras等人，2024）、视频生成（Dehghani等人，2023）、文本到图像生成（Rombach等人，2022；Betker等人，2023）、语音合成（Song等人，2022）以及文本到3D生成（Poole等人，2022；Lin等人，2023）在内的多个领域展现出卓越的建模能力。它们已成为推动深度生成模型发展的关键驱动力。DPMs通过正向过程向图像中引入噪声，然后利用神经网络学习反向过程，逐步去除噪声，从而生成图像（Ho等人，2020；Song等人，2020b）。与生成对抗网络（GANs）（Goodfellow等人，2014）和变分自编码器（VAEs）（Kingma和Welling，2013）等其他生成方法相比，DPMs不仅优化目标更简单，还能够生成更高质量的样本（Dhariwal和Nichol，2021）。然而，通过DPMs生成高质量样本需要数百甚至数千个去噪步骤，这大大降低了它们的采样效率，成为其广泛应用的主要障碍。
目前，DPMs中快速采样的现有技术主要分为两类。第一类是基于训练的方法（Salimans和Ho，2022；Liu等人，2022b；Song等人，2023；Yin等人，2024），这类方法可以显著压缩采样步骤，甚至实现单步采样。然而，这种压缩通常伴随着相当大的额外训练成本，并且这些方法难以应用于大型预训练模型。第二类是无需训练的采样器（Song等人，2020a；Lu等人，2022a、b；Bao等人，2022b、a；Liu等人，2022a；Li等人，2023；Zheng等人，2023；Ma等人，2024；Wimbauer等人，2024；Zhao等人，2023；Xue等人，2023），它们通常采用随机微分方程（SDE）/常微分方程（ODE）的隐式或解析解来实现低误差的采样过程。例如，Lu等人（Lu等人，2022a、b）通过分析DPMs的ODE求解器的半线性结构，试图解析地推导出DPMs的ODE求解器的最优解。这些无需训练的采样策略通常可以即插即用，与现有的预训练DPMs兼容。然而，当NFE低于10时，这些无需训练的方法的离散化误差会显著放大，导致收敛问题（Lu等人，2022a、b），并且仍然可能很耗时。
为了进一步提高DPMs的采样速度，我们分析了现有无需训练的加速方法的改进潜力。最初，我们观察到当时间步长Δt不是极大时，现有ODE求解器的模型输出具有很高的相似性，如图1a所示。这一观察结果促使我们利用过去时间步计算出的分数来近似当前分数，从而预测一个 “跳板” 状态。此外，正如备注1中所指出的，由于DPMs的采样过程与随机梯度下降（SGD）（Robbins和Monro，1951）之间存在相似性，我们引入了受Nesterov动量（Nesterov，1983）启发的前瞻更新机制，该机制以加速SGD训练而闻名。具体来说，我们首先使用 “跳板” 状态预测未来分数以减少误差，如图1b所示。然后，我们进一步用未来分数替换当前分数，以便采用更大的更新步长Δt，如图1c所示。
受这些见解的启发，我们提出了PFDiff，这是一种跳步采样算法，它结合过去和未来的分数快速更新当前的中间状态。值得注意的是，PFDiff无需训练，并且与现有的DPMs采样算法正交，为DPMs采样提供了一个新的正交维度。此外，我们证明了PFDiff尽管使用较少的NFE，但能够校正一阶ODE求解器采样轨迹中的误差，如图1c所示。这确保了在提高采样速度的同时不会牺牲采样质量；它只是减少了现有ODE求解器中不必要的NFE。为了验证PFDiff的正交性和有效性，我们在无条件（Ho等人，2020；Song等人，2020b、a）和有条件（Dhariwal和Nichol，2021；Rombach等人，2022）预训练的DPMs上进行了广泛的实验。可视化实验结果见附录D.9。结果表明，PFDiff显著提高了现有ODE求解器的采样性能。特别是在条件DPMs中，仅以DDIM为基线的PFDiff就超越了以往最先进的无需训练的采样算法。 

### 2. 背景
#### 2.1 扩散随机微分方程
![f1](f1.png) 
*图1：(a) 噪声网络输出$\epsilon_{\theta}(x_{t}, t)$的均方误差（MSE）随时间步长$\Delta t$的变化趋势，其中$\eta$来自公式(6)中的$\bar{\sigma}_{t}$。实线：ODE求解器，虚线：SDE求解器。(b) 分别使用 “跳板” $\tilde{x}_{t_{i+h}}$和未来分数$\epsilon_{\theta}(\tilde{x}_{t_{i+h}}, t_{i+h})$更新状态的均方误差，相对于1000次函数评估（NFE）的采样过程，计算公式为：$\left\|\tilde{x}_{t_{i+(k+1)}}-\tilde{x}_{t_{i+(k+1)}}^{gt}\right\|^{2}$。(c) PFDiff-1与一阶ODE求解器的部分采样轨迹对比，其中更新方向由采样轨迹的切线方向引导* 

扩散概率模型（DPMs）（Sohl-Dickstein等人，2015；Ho等人，2020；Song等人，2020b）旨在生成服从数据分布$q(x_{0})$的$D$维随机变量$x_{0} \in \mathbb{R}^{D}$。以去噪扩散概率模型（DDPM）（Ho等人，2020）为例，这些模型通过在离散时间步上定义的正向过程向数据分布引入噪声，逐渐将其转化为标准高斯分布$x_{T} \sim N(0, I)$。正向过程的潜在变量$\{x_{t}\}_{t \in[0, T]}$定义如下：
$$q(x_{t}|x_{0})=\mathcal{N}(x_{t}|\alpha_{t}x_{0}, \sigma_{t}^{2}I) \tag{1}$$
其中$\alpha_{t}$是与时间步$t$相关的标量函数，且$\alpha_{t}^{2}+\sigma_{t}^{2}=1$。在模型的反向过程中，DDPM利用神经网络模型$p_{\theta}(x_{t - 1}|x_{t})$来近似转移概率$q(x_{t - 1}|x_{t}, x_{0})$：
$$p_{\theta}(x_{t - 1}|x_{t})=\mathcal{N}(x_{t - 1}|\mu_{\theta}(x_{t}, t), \sigma_{\theta}^{2}(t)I) \tag{2}$$
通过从标准高斯分布采样并利用训练好的神经网络，可以生成服从数据分布$p_{\theta}(x_{0})=\prod_{t = 1}^{T}p_{\theta}(x_{t - 1}|x_{t})$的样本。

此外，Song等人（2020b）引入随机微分方程（SDE）来对连续时间步的DPMs进行建模，其正向过程定义为：
$$dx_{t}=f(t)x_{t}dt + g(t)dw_{t}, \quad x_{0} \sim q(x_{0}) \tag{3}$$
其中$w_{t}$表示标准维纳过程，$f$和$g$是时间步$t$的标量函数。值得注意的是，公式（1）中的正向过程是公式（3）的离散形式，其中$f(t)=\frac{d\log\alpha_{t}}{dt}$，$g^{2}(t)=\frac{d\sigma_{t}^{2}}{dt}-2\frac{d\log\alpha_{t}}{dt}\sigma_{t}^{2}$ 。Song等人（2020b）进一步证明，公式（3）中的正向过程存在一个从时间步$T$到$0$的等效反向过程：
$$dx_{t}=[f(t)x_{t}-g^{2}(t)\nabla_{x}\log q_{t}(x_{t})]dt + g(t)d\overline{w}_{t}, \quad x_{T} \sim q(x_{T}) tag{4}$$
其中$\overline{w}$表示标准维纳过程。在这个反向过程中，唯一未知的是得分函数$\nabla_{x}\log q_{t}(x_{t})$，它可以通过神经网络进行近似。

#### 2.2 扩散常微分方程
在基于SDE的DPMs中，采样过程的离散化通常需要大量时间步才能收敛，例如DDPM（Ho等人，2020）中使用的$T = 1000$个时间步。这主要是因为SDE在每个时间步引入了随机性。为了实现更高效的采样过程，Song等人（2020b）利用福克 - 普朗克方程（Oksendal和Oksendal，2003）推导出与SDE相关的概率流常微分方程（ODE），该ODE在任何给定时间$t$与SDE具有相同的边际分布。具体来说，从公式（3）推导得到的反向过程ODE可以表示为：
$$dx_{t}=[f(t)x_{t}-\frac{1}{2}g^{2}(t)\nabla_{x}\log q_{t}(x_{t})]dt, \quad x_{T} \sim q(x_{T}) \tag{5}$$
与SDE不同，ODE避免了随机性的引入，从而可以在更少的时间步内收敛到数据分布。Song等人（2020b）采用高阶RK45 ODE求解器（Dormand和Prince，1980），仅用60次函数评估（NFE）就实现了与1000次NFE的SDE相当的样本质量。此外，像DDIM（Song等人，2020a）和DPM-Solver（Lu等人，2022a）等研究探索了能够在更少NFE下收敛的离散ODE形式。对于DDIM，它在DDPM的基础上打破了马尔可夫链约束，推导出新的采样公式：
$$x_{t - 1}=\sqrt{\alpha_{t - 1}}(\frac{x_{t}-\sqrt{1 - \alpha_{t}}\epsilon_{\theta}(x_{t}, t)}{\sqrt{\alpha_{t}}})+\sqrt{1 - \alpha_{t - 1}-\overline{\sigma}_{t}^{2}}\epsilon_{\theta}(x_{t}, t)+\overline{\sigma}_{t}\epsilon_{t} \tag{6}$$
其中$\overline{\sigma}_{t}=\eta\sqrt{\frac{1 - \alpha_{t - 1}}{1 - \alpha_{t}}}\sqrt{1 - \frac{\alpha_{t}}{\alpha_{t - 1}}}$，$\alpha_{t}$对应公式（1）中的$\alpha_{t}^{2}$。当$\eta = 1$时，公式（6）变为DDPM的形式；当$\eta = 0$时，它退化为ODE，即DDIM采用的形式，能够在更少的时间步内获得高质量样本。

**备注1**：在本文中，我们认为得分$d\overline{x}_{t}$、噪声网络输出$\epsilon_{\theta}(x_{t}, t)$和得分函数$\nabla_{x}\log q_{t}(x_{t})$表达的是等效概念。这是因为Song等人（2020b）证明了$\epsilon_{\theta}(x_{t}, t)=-\sigma_{t}\nabla_{x}\log q_{t}(x_{t})$。此外，我们发现DPMs的任何一阶求解器都可以参数化为$x_{t - 1}=\overline{x}_{t}-\gamma_{t}d\overline{x}_{t}+\xi\epsilon_{t}$。以DDIM（Song等人，2020a）为例，其中$\overline{x}_{t}=\sqrt{\frac{\alpha_{t - 1}}{\alpha_{t}}}x_{t}$，$\gamma_{t}=\sqrt{\frac{\alpha_{t - 1}}{\alpha_{t}}-\alpha_{t - 1}}-\sqrt{1 - \alpha_{t - 1}}$，$d\overline{x}_{t}=\epsilon_{\theta}(x_{t}, t)$，$\xi = 0$。这表明了SGD与DPMs采样过程之间的相似性，Xue等人（2023）和Wang等人（2024）的研究也隐含地暗示了这一发现。 

