# Formal Methods and Machine Learning

This repository contains a list of research links for the intersection
of Formal Methods and Machine Learning.

For applied machine learning for formal methods, some references to machine
learning for general software development are included as well,
which might be applicable for formal methods.
Analogously, articles concerning the verification of arbitrary (black-box)
systems are listed, which can be expanded onto machine learning systems.

The entries are (mostly) sorted by
publication year (descending),
authors (ascending),
title (ascending).

<!-- TOC depthFrom:2 depthTo:4 -->

- [1. Applied Machine Learning for Formal Methods](#1-applied-machine-learning-for-formal-methods)
  - [1.1. Tool and Configuration Selection](#11-tool-and-configuration-selection)
  - [1.2. Synthesis and Repair](#12-synthesis-and-repair)
  - [1.3. Feature Selection](#13-feature-selection)
  - [1.4. Model Checking](#14-model-checking)
  - [1.5. Automated Theorem Proving](#15-automated-theorem-proving)
  - [1.6. Invariant Learning](#16-invariant-learning)
  - [1.7. Applied ML for General Software Development](#17-applied-ml-for-general-software-development)
  - [1.8. Artificial Intelligence for Formal Software Development](#18-artificial-intelligence-for-formal-software-development)
- [2. Applied Formal Methods for Machine Learning](#2-applied-formal-methods-for-machine-learning)
  - [2.1. Neural Networks](#21-neural-networks)
  - [2.2. Reinforcement Learning](#22-reinforcement-learning)
  - [2.3. Runtime Enforcement and Shield Synthesis](#23-runtime-enforcement-and-shield-synthesis)
  - [2.4. Markov Chains and Markov Decision Procedures](#24-markov-chains-and-markov-decision-procedures)
  - [2.5. Clustering](#25-clustering)
  - [2.6. Machine Learning Systems](#26-machine-learning-systems)
  - [2.7. Cyber-Physical Systems](#27-cyber-physical-systems)
- [3. Integrated Approaches](#3-integrated-approaches)
  - [3.1. Executable Specifications](#31-executable-specifications)
  - [3.2. Cyber-Physical Systems](#32-cyber-physical-systems)
  - [3.3. Pattern Recognition](#33-pattern-recognition)
- [4. Unsorted Online Sources](#4-unsorted-online-sources)
  - [4.1. Courses](#41-courses)

<!-- /TOC -->

## 1. Applied Machine Learning for Formal Methods

### 1.1. Tool and Configuration Selection

- "Automated Backend Selection for ProB Using Deep Learning"
  Dunkelau et al. (2019)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-20652-9_9)]
  [[doi](https://doi.org/10.1007/978-3-030-20652-9_9)]
- "PaMpeR: Proof Method Recommendation System for Isabelle/HOL"
  Nagashima & He (2018)
  [[link](https://dl.acm.org/doi/abs/10.1145/3238147.3238210)]
  [[pdf](https://arxiv.org/pdf/1806.07239)]
  [[doi](https://doi.org/10.1145/3238147.3238210)]
- "MUX: Algorithm Selection for Software Model Checkers",
  Tulsian et al. (2014)
  [[link](https://dl.acm.org/doi/abs/10.1145/2597073.2597080)]
  [[pdf](https://www.researchgate.net/profile/Varun_Tulsian/publication/265416309_MUX_Algorithm_Selection_for_Software_Model_Checkers/links/540eab3c0cf2f2b29a3a91a9.pdf)]
  [[doi](https://doi.org/10.1145/2597073.2597080)]
- "Evaluating the use of a general-purpose benchmark suite for domain-specific
  SMT-solving",
  Healy et al. (2016)
  [[link](https://dl.acm.org/doi/abs/10.1145/2851613.2851975)]
  [[pdf](http://mural.maynoothuniversity.ie/10223/1/JP-Evaluating-2016.pdf)]
  [[doi](https://doi.org/10.1145/2851613.2851975)]
- "ParamILS: An Automatic Algorithm Configuration Framework"
  Hutter et al. (2009)
  [[link](https://www.jair.org/index.php/jair/article/view/10628)]
  [[pdf](https://www.jair.org/index.php/jair/article/download/10628/25415/)]
  [[doi](https://doi.org/10.1613/jair.2861)]
- "Machine learning and automated theorem proving",
  Bridge (2010)
  [[link](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-792.html)]
  [[pdf](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-792.pdf)]

### 1.2. Synthesis and Repair

- "Automatic B-model repair using model checking and machine learning",
  Cai et al. (2019)
  [[link](https://link.springer.com/article/10.1007/s10515-019-00264-4)]
  [[doi](https://doi.org/10.1007/s10515-019-00264-4)]
- "Repair and Generation of Formal Models Using Synthesis",
  Schmidt et al. (2018)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-98938-9_20)]
  [[pdf](https://www.krin.gs/publication/schmidt-model-repair-ifm18/schmidt-model-repair-ifm18.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-98938-9_20)]
- "A Supervisory Control Algorithm Based on Property-Directed Reachability",
  Claessen et al. (2017)
  [[link](https://arxiv.org/abs/1711.06501)]
  [[pdf](https://arxiv.org/pdf/1711.06501)]
- "A theory of formal synthesis via inductive learning",
  Jha & Seshia (2017)
  [[link](https://link.springer.com/article/10.1007/s00236-017-0294-5)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/s00236-017-0294-5.pdf)]
  [[doi](https://doi.org/10.1007/s00236-017-0294-5)]
- "Model Checking-Based Genetic Programming with an Application to
  Mutual Exclusion",
  Katz & Peled (2008)
  [[link](https://link.springer.com/chapter/10.1007/978-3-540-78800-3_11)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-540-78800-3_11.pdf)]
  [[doi](https://doi.org/10.1007/978-3-540-78800-3_11)]

### 1.3. Feature Selection

- "Efficient Semantic Features for Automated Reasoning over Large Theories",
  Kaliszyk et al. (2015)
  [[pdf](https://repository.ubn.ru.nl/bitstream/handle/2066/143635/143635.pdf)]

### 1.4. Model Checking

- "LTL Model Checking Based on Binary Classification of Machine Learning",
  Zhu et al. (2019)
  [[link](https://ieeexplore.ieee.org/document/8845603)]
  [[pdf](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8845603)]
  [[doi](https://doi.org/10.1109/ACCESS.2019.2942762)]
- "Machine Learning Methods in Statistical ModelChecking and System Design -
   Tutorial",
  Bortolussi et al. (2015)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-23820-3_23)]
  [[pdf](https://arts.units.it/retrieve/handle/11368/2860877/69589/RV2015_tutorial-post.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-23820-3_23)]
- "Verification of Markov Decision Processes using Learning Algorithms",
  Brázdil et al. (2015)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-11936-6_8)]
  [[pdf](https://arxiv.org/pdf/1402.2967.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-11936-6_8)]
- "Heuristic Model Checking using a Monte-Carlo Tree SearchAlgorithm"
  Poulding & Feldt (2015)
  [[link](https://dl.acm.org/doi/abs/10.1145/2739480.2754767)]
  [[doi](https://doi.org/10.1145/2739480.2754767)]
- "Bounded Rational Search for On-the-fly ModelChecking of LTL Properties"
  Behjati et al. (2009)
  [[link](https://link.springer.com/chapter/10.1007/978-3-642-11623-0_17)]
  [[pdf](https://www.researchgate.net/profile/Razieh_Behjati/publication/220843703_Bounded_Rational_Search_for_On-the-Fly_Model_Checking_of_LTL_Properties/links/54f23ce60cf2b36214afee38/Bounded-Rational-Search-for-On-the-Fly-Model-Checking-of-LTL-Properties.pdf)]
  [[doi](https://doi.org/10.1007/978-3-642-11623-0_17)]
- "Enhancing model checking in verification by AI techniques"
  Buccafurri et al. (1999)
  [[link](https://www.sciencedirect.com/science/article/pii/S0004370299000399)]
  [[pdf](https://www.sciencedirect.com/science/article/pii/S0004370299000399/pdf?md5=50a73104607ae4fe280b602eb3fab87e&pid=1-s2.0-S0004370299000399-main.pdf&_valck=1)]

### 1.5. Automated Theorem Proving

- "Machine Learning for Instance Selection in SMT Solving",
  Blanchette et al. (2019)
  [[link](https://hal.archives-ouvertes.fr/hal-02381430/)]
  [[pdf](https://hal.archives-ouvertes.fr/hal-02381430/file/paper.pdf)]
- "Guiding High-Performance SAT Solvers with Unsat-Core Predictions",
  Selsam & Bjørner (2019)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-24258-9_24)]
  [[pdf](https://arxiv.org/pdf/1903.04671)]
  [[doi](https://doi.org/10.1007/978-3-030-24258-9_24)]
- "Learning A SAT Solver from Single-Bit Supervision"
  Selsam et al. (2019)
  [[link](https://arxiv.org/abs/1802.03685)]
  [[pdf](https://arxiv.org/pdf/1802.03685)]
- "Reinforcement Learning of Theorem Proving",
  Kaliszyk et al. (2018)
  [[link](http://papers.nips.cc/paper/8098-reinforcement-learning-of-theorem-proving)]
  [[pdf](https://papers.nips.cc/paper/8098-reinforcement-learning-of-theorem-proving.pdf)]
- "Learning-assisted theorem proving with millions of lemmas"
  Kaliszyk & Urban (2015)
  [[link](https://www.sciencedirect.com/science/article/pii/S074771711400100X)]
  [[pdf](https://www.sciencedirect.com/science/article/pii/S074771711400100X)]
  [[doi](https://doi.org/10.1016/j.jsc.2014.09.032)]
- "A Survey of Axiom Selection as a Machine Learning Problem",
  Blanchette & Kühlwein (2014)
  [[pdf](https://www.cs.vu.nl/~jbe248/axiom_sel.pdf)]
- "Stronger Automation for Flyspeck by Feature Weighting and Strategy Evolution",
  Kaliszyk & Urban (2013)
  [[link](https://hdl.handle.net/2066/119984)]
  [[pdf](https://repository.ubn.ru.nl/bitstream/handle/2066/119984/119984.pdf)]
- "Overview and Evaluation of Premise Selection Techniques for
  Large Theory Mathematics"
  Kühlwein et al. (2012)
  [[link](https://link.springer.com/chapter/10.1007/978-3-642-31365-3_30)]
  [[pdf](http://grid01.ciirc.cvut.cz/~mptp/premisealgos.pdf)]
  [[doi](https://doi.org/10.1007/978-3-642-31365-3_30)]
- "Theorem Proving in Large Formal Mathematics as an Emerging AI Field",
  Urban & Vyskočil (2012)
  [[link](https://link.springer.com/chapter/10.1007/978-3-642-36675-8_13)]
  [[pdf](https://arxiv.org/pdf/1209.3914)]
  [[doi](https://doi.org/10.1007/978-3-642-31365-3_30)]

### 1.6. Invariant Learning

- "Synthesizing Environment Invariants for Modular Hardware Verification",
  Zhang et al. (2020)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-39322-9_10)]
  [[pdf](https://bo-yuan-huang.github.io/ILAng-Doc/vmcai20.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-39322-9_10)]
- "Quantified Invariants via Syntax-Guided Synthesis",
  Fedyukovich et al. (2019)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-25540-4_14)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-030-25540-4_14.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-25540-4_14)]
- "Property Directed Inference of Relational Invariants",
  Mordvinov & Fedyukovich (2019)
  [[link](https://ieeexplore.ieee.org/abstract/document/8894274/)]
  [[pdf](https://www.cs.fsu.edu/~grigory/relspacer.pdf)]
  [[doi](https://doi.org/10.23919/FMCAD.2019.8894274)]
- "IC3 - Flipping the E in ICE",
  Vizel et al. (2017)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-52234-0_28)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-319-52234-0_28.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-52234-0_28)]
- "ICE: A Robust Framework for Learning Invariants",
  Garg et al. (2014)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-08867-9_5)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-319-08867-9_5.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-08867-9_5)]
- "Learning Universally Quantified Invariants of Linear Data Structures",
  Garg et al. (2013)
  [[link](https://link.springer.com/chapter/10.1007/978-3-642-39799-8_57)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-642-39799-8_57.pdf)]
  [[doi](https://doi.org/10.1007/978-3-642-39799-8_57)]

### 1.7. Applied ML for General Software Development

- "Machine Learning for Software Engineering: A Systematic Mapping",
  Shafiq et al. (2020)
  [[link](https://arxiv.org/abs/2005.13299)]
  [[pdf](https://arxiv.org/pdf/2005.13299)]
- "Awesome Machine Learning On Source Code"
  [[link](https://github.com/src-d/awesome-machine-learning-on-source-code)]

### 1.8. Artificial Intelligence for Formal Software Development

- "AI meets Formal Software Development",
  Bundy et al. (2012),
  [[link](https://drops.dagstuhl.de/opus/volltexte/2012/3731/)]
  [[pdf](https://drops.dagstuhl.de/opus/volltexte/2012/3731/pdf/dagrep_v002_i007_p001_s12271.pdf)]
  [[doi](https://doi.org/10.4230/DagRep.2.7.1)]

## 2. Applied Formal Methods for Machine Learning

### 2.1. Neural Networks

- "Improved Geometric Path Enumeration for Verifying ReLU Neural Networks",
  Bak et al. (2020)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-53288-8_4)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-030-53288-8_4.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-53288-8_4)]
- "NNV: The Neural Network Verification Tool for Deep Neural Networks and
  Learning-Enabled Cyber-Physical Systems",
  Tran et al. (2020)
  [[link](https://arxiv.org/abs/2004.05519)]
  [[pdf](https://arxiv.org/pdf/2004.05519)]
- "Verification of Deep Convolutional Neural Networks Using ImageStars",
  Tran et al. (2020)
  [[link](https://arxiv.org/abs/2004.05511)]
  [[pdf](https://arxiv.org/pdf/2004.05511)]
- "A Game-Based Approximate Verification of Deep Neural Networks with
  Provable Guarantees",
  Wu et al. (2020)
  [[link](https://www.sciencedirect.com/science/article/pii/S0304397519304426)]
  [[pdf](https://arxiv.org/pdf/1807.03571)]
  [[doi](https://doi.org/10.1016/j.tcs.2019.05.046)]
- "A Formalization of Robustness for Deep Neural Networks",
  Dreossi et al. (2019)
  [[link](https://arxiv.org/abs/1903.10033)]
  [[pdf](https://arxiv.org/pdf/1903.10033)]
- "A Survey of Safety and Trustworthiness of Deep Neural Networks",
  Huang et al. (2019)
  [[link](https://arxiv.org/abs/1812.08342)]
  [[pdf](https://arxiv.org/pdf/1812.08342)]
- "The Marabou Framework for Verification and Analysis of Deep Neural Networks",
  Katz et al. (2019)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-25540-4_26)]
  [[pdf](https://link.springer.com/content/pdf/10.1007%2F978-3-030-25540-4_26.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-25540-4_26)]
- "Algorithms for Verifying Deep Neural Networks",
  Liu et al. (2019)
  [[link](https://arxiv.org/abs/1903.06758)]
  [[pdf](https://arxiv.org/pdf/1903.06758)]
- "Bringing Engineering Rigor to Deep Learning",
  Pei et al. (2019)
  [[link](https://dl.acm.org/doi/abs/10.1145/3352020.3352030)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3352020.3352030)]
  [[doi](https://doi.org/10.1145/3352020.3352030)]
- "Star-Based Reachability Analysis of Deep Neural Networks",
  Tran et al. (2019)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-30942-8_39)]
  [[pdf](https://www.researchgate.net/profile/Dung_Tran10/publication/333759458_Star-Based_Reachability_Analysis_of_Deep_Neural_Networks/links/5d04f416a6fdcc39f11ca50c/Star-Based-Reachability-Analysis-of-Deep-Neural-Networks.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-30942-8_39)]
- "Semantic Adversarial Deep Learning",
  Dreossi et al. (2018)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-96145-3_1)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-319-96145-3_1.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-96145-3_1)]
- "AI2: Safety and Robustness Certification of Neural Networks with Abstract Interpretation"
  Gehr et al. (2018)
  [[link](https://ieeexplore.ieee.org/abstract/document/8418593)]
  [[pdf](https://files.sri.inf.ethz.ch/website/papers/sp2018.pdf)]
  [[doi](https://doi.org/10.1109/SP.2018.00058)]
- "Reachability Analysis of Deep Neural Networks with Provable Guarantees",
  Ruan et al. (2018)
  [[link](https://arxiv.org/abs/1805.02242)]
  [[pdf](https://arxiv.org/pdf/1805.02242)]
- "Formal Specification for Deep Neural Networks",
  Seshia et al. (2018)
  [[link](https://link.springer.com/chapter/10.1007/978-3-030-01090-4_2)]
  [[pdf](https://digitalassets.lib.berkeley.edu/techreports/ucb/text/EECS-2018-25.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-01090-4_2)]
- "Formal Security Analysis of Neural Networks using Symbolic Intervals",
  Wang et al. (2018)
  [[link](https://www.usenix.org/conference/usenixsecurity18/presentation/wang-shiqi)]
  [[pdf](https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-wang_0.pdf)]
  [[video](https://youtu.be/jm_7SKOC-cA)]
- "Provable Defenses against Adversarial Examples via the Convex Outer
  Adversarial Poly-tope",
  Wong & Kolter (2018)
  [[link](http://proceedings.mlr.press/v80/wong18a.html)]
  [[pdf](http://proceedings.mlr.press/v80/wong18a/wong18a.pdf)]
- "Specification-Guided Safety Verification for Feedforward Neural Networks",
  Xiang et al. (2018)
  [[link](https://arxiv.org/abs/1812.06161)]
  [[pdf](https://arxiv.org/pdf/1812.06161)]
- "Verification for Machine Learning, Autonomy, and Neural Networks Survey",
  Xiang et al. (2018)
  [[link](https://arxiv.org/abs/1810.01989)]
  [[pdf](https://arxiv.org/pdf/1810.01989)]
- "Output Range Analysis for Deep Neural Networks",
  Dutta et al. (2017)
  [[link](https://arxiv.org/abs/1709.09130)]
  [[pdf](https://arxiv.org/pdf/1709.09130)]
- "Safety Verification of Deep Neural Networks",
  Huang et al. (2017)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-63387-9_1)]
  [[pdf](https://arxiv.org/pdf/1610.06940.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-63387-9_1)]
- "Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks",
  Katz et al. (2017)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-63387-9_5)]
  [[pdf](https://arxiv.org/pdf/1702.01135.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-63387-9_5)]
- "Verifying Properties of BNinarized Deep Neural Networks",
  Narodytska et al. (2017)
  [[link](https://arxiv.org/abs/1709.06662)]
  [[pdf](https://arxiv.org/pdf/1709.06662.pdf)]
- "DeepXplore: Automated Whitebox Testing of Deep Learning Systems",
  Pei et al. (2017)
  [[link](https://arxiv.org/abs/1705.06640)]
  [[pdf](https://arxiv.org/pdf/1705.06640)]
- "DeepTest: Automated Testing of Deep-Neural-Network-driven Autonomous Cars",
  Tian et al. (2017)
  [[link](https://dl.acm.org/doi/abs/10.1145/3180155.3180220)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3180155.3180220)]
  [[doi](https://doi.org/10.1145/3180155.3180220)]
- "Measuring Neural Net Robustness with Constraints",
  Bastani et al. (2016)
  [[link](http://papers.nips.cc/paper/6339-measuring-neural-net-robustness-with-constraints)]
  [[pdf](http://papers.nips.cc/paper/6339-measuring-neural-net-robustness-with-constraints.pdf)]
- "Towards Verification of Artificial Neural Networs",
  Scheibler et al. (2015)
  [[pdf](https://slub.qucosa.de/api/qucosa%3A5018/attachment/ATT-0/?L=1#page=30)]
- "Challenging SMT solvers to verify neural networks",
  Pulina & Tacchella (2012)
  [[link](https://content.iospress.com/articles/ai-communications/aic525)]
  [[pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.866.7776&rep=rep1&type=pdf)]
  [[doi](https://doi.org/10.3233/AIC-2012-0525)]
- "An Abstraction-Refinement Approach to Verification of
  Artificial Neural Networks",
  Pulina & Tacchella (2010)
  [[link](https://link.springer.com/chapter/10.1007/978-3-642-14295-6_24)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-642-14295-6_24.pdf)]
  [[doi](https://doi.org/10.1007/978-3-642-14295-6_24)]

### 2.2. Reinforcement Learning

- "Safe Reinforcement Learning Using Probabilistic Shields",
  Jansen et al. (2020)
  [[link](https://drops.dagstuhl.de/opus/volltexte/2020/12815/)]
  [[pdf](https://drops.dagstuhl.de/opus/volltexte/2020/12815/pdf/LIPIcs-CONCUR-2020-3.pdf)]
  [[doi](https://doi.org/10.4230/LIPIcs.CONCUR.2020.3)]
- "Safety Aware Reinforcement Learning (SARL)",
  Miret et al. (2020)
  [[link](https://arxiv.org/abs/2010.02846)]
  [[pdf](https://arxiv.org/pdf/2010.02846.pdf)]
- "Safe Reinforcement Learning via Shielding",
  Alshiekh et al. (2018)
  [[link](https://graz.pure.elsevier.com/en/publications/safe-reinforcement-learning-via-shielding)]
  [[pdf](https://viterbi-web.usc.edu/~jdeshmuk/teaching/cs699-fm-for-cps/Papers/C2.pdf)]
- "Safe Reinforcement Learning via Formal Methods",
  Fulton & Platzer (2018)
  [[pdf](http://www.cs.cmu.edu/~aplatzer/pub/SafeRL.pdf)]
- "Safe Model-based Reinforcement Learning withStability Guarantees",
  Berkenkamp et al. (2017)
  [[link](http://proceedings.mlr.press/v97/ustun19a)]
  [[pdf](https://papers.nips.cc/paper/6692-safe-model-based-reinforcement-learning-with-stability-guarantees.pdf)]
- "Safety-Constrained Reinforcement Learning for MDPs",
  Jungens et al. (2016)
  [[link](https://link.springer.com/chapter/10.1007/978-3-662-49674-9_8)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-662-49674-9_8.pdf)]
  [[doi](https://doi.org/10.1007/978-3-662-49674-9_8)]
- "A comprehensive survey on safe reinforcement learning",
  García & Fernández (2015)
  [[link](https://dl.acm.org/doi/10.5555/2789272.2886795)]
  [[pdf](https://dl.acm.org/doi/pdf/10.5555/2789272.2886795)]
  [[doi](https://doi.org/10.5555/2789272.2886795)]
- "Reachability-based safe learning with Gaussian processes",
  Akametalu et al. (2014)
  [[link](https://ieeexplore.ieee.org/abstract/document/7039601/))]
  [[pdf](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-190.pdf)]
  [[doi](https://doi.org/10.1109/CDC.2014.7039601)]
- "Smart Exploration in Reinforcement LEarning using Absolute Temporal
  Difference Errors",
  Gehring & Precup (2013)
  [[pdf](http://www.ifaamas.org/Proceedings/aamas2013/docs/p1037.pdf)]
- "Safe Exploration in Markov Decision Processes",
  Moldovan & Abbeel (2012)
  [[link](https://arxiv.org/abs/1205.4810)]
  [[pdf](https://arxiv.org/pdf/1205.4810.pdf)]
- "Safe Exploration for Reinforcement Learning",
  Hans et al. (2008)
  [[pdf](https://www.tu-ilmenau.de/fileadmin/media/neurob/publications/conferences_int/2008/Hans-ESANN-08.pdf)]

### 2.3. Runtime Enforcement and Shield Synthesis

- "Shield Synthesis for Real: Enforcing Safety in Cyber-Physical Systems",
  Wu et al. (2019)
  [[link](https://ieeexplore.ieee.org/abstract/document/8894264/)]
  [[pdf](https://arxiv.org/pdf/1908.05402.pdf)]
  [[doi](https://doi.org/10.23919/FMCAD.2019.8894264)]
- "Shield synthesis",
  Könighofer et al. (2017)
  [[link](https://link.springer.com/article/10.1007/s10703-017-0276-9)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-662-46681-0_51.pdf)]
  [[doi](https://doi.org/10.1007/s10703-017-0276-9)]
- "Runtime enforcement using Büchi Games",
  Renard et al. (2017)
  [[link](https://dl.acm.org/doi/abs/10.1145/3092282.3092296)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3092282.3092296)]
  [[doi](https://doi.org/10.1145/3092282.3092296)]
- "Shield Synthesis: Runtime Enforcement for Reactive Systems",
  Bloem et al. (2015)
  [[link](https://link.springer.com/chapter/10.1007/978-3-662-46681-0_51)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/978-3-662-46681-0_51.pdf)]
  [[doi](https://doi.org/10.1007/978-3-662-46681-0_51)]
- "Enforcement of (Timed) Properties with Uncontrollable Events",
  Renard et al. (2015)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-25150-9_31)]
  [[pdf](https://hal.inria.fr/hal-01185238/document)]
  [[doi](https://doi.org/10.1007/978-3-319-25150-9_31)]
- "Runtime Verification for LTL and TLTL",
  Bauer et al. (2011)
  [[link](https://dl.acm.org/doi/abs/10.1145/2000799.2000800)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/2000799.2000800)]
  [[doi](https://doi.org/10.1145/2000799.2000800)]

### 2.4. Markov Chains and Markov Decision Procedures

- "Smoothed model checking for uncertain Continuous-Time Markov Chains",
  Bortolussi et al. (2016)
  [[link](https://www.sciencedirect.com/science/article/pii/S0890540116000055)]
  [[pdf](https://arxiv.org/pdf/1402.1450)]
  [[doi](https://doi.org/10.1016/j.ic.2016.01.004)]
- "Counterexample Explanation by Learning Small Strategies in Markov Decision Processes",
  Brázdil et al. (2015)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-21690-4_10)]
  [[pdf](https://link.springer.com/content/pdf/10.1007%2F978-3-319-21690-4_10.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-21690-4_10)]

### 2.5. Clustering

- "A Formal Algorithm for Verifying the Validity of Clustering Results Based
  on Model Checking",
  Huang et al. (2014)
  [[link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090109)]
  [[pdf](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0090109&type=printable)]
  [[doi](https://doi.org/10.1371/journal.pone.0090109)]

### 2.6. Machine Learning Systems

- "Towards Verified Stochastic Variational Inference forProbabilistic Programs",
  Lee et al. (2020)
  [[link](https://dl.acm.org/doi/abs/10.1145/3371084))]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3371084)]
  [[doi](https://doi.org/10.1145/3371084)]
- "Towards Verified Artificial Intelligence",
  Seshia et al. (2020)
  [[link](https://arxiv.org/abs/1606.08514v4)]
  [[pdf](https://arxiv.org/pdf/1606.08514v4.pdf)]
- "Certifying the True Error: Machine Learning in Coq with Verified
  Generalization Guarantees",
  Bagnall & Stewart (2019)
  [[link](https://www.aaai.org/ojs/index.php/AAAI/article/view/4115)]
  [[pdf](https://www.aaai.org/ojs/index.php/AAAI/article/view/4115/3993)]
  [[doi](https://doi.org/10.1609/aaai.v33i01.33012662)]
- "VerifAI: A Toolkit for the Formal Design and Analysisof Artificial
  Intelligence-Based Systems",
  Dreossi et al. (2019)
  [[link](https://people.eecs.berkeley.edu/~sseshia/pubs/b2hd-verifai-cav19.html)]
  [[pdf](https://people.eecs.berkeley.edu/~sseshia/pubdir/verifai-cav19.pdf)]
  [[github](https://github.com/BerkeleyLearnVerify/VerifAI)]
- "Proving Expected Sensitivity of Probabilistic Programs", Barthe et al. (2018)
  [[link](https://dl.acm.org/doi/abs/10.1145/3158145)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3158145)]
  [[doi](https://doi.org/10.1145/3158145)]
- "The challenge of verification and testing of machine learning",
  Goodfellow & Papernot (2017)
  [[html](http://www.cleverhans.io/security/privacy/ml/2017/06/14/verification.html)]
- "Verification and control of partially observable probabilistic systems",
  Norman et al. (2017)
  [[link](https://link.springer.com/article/10.1007/s11241-017-9269-4)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/s11241-017-9269-4.pdf)]
  [[doi](https://doi.org/10.1007/s11241-017-9269-4)]
- "Developing Bug-Free Machine Learning Systems With Formal Mathematics",
  Selsam et al. (2017)
  [[link](https://arxiv.org/abs/1706.08605)]
  [[pdf](https://arxiv.org/pdf/1706.08605)]
- "Concrete Problems in AI Safety",
  Amodai et al. (2016)
  [[link](http://arxiv.org/abs/1606.06565)]
  [[pdf](http://arxiv.org/pdf/1606.06565.pdf)]
  [[doi](https://doi.org/)]
- "SoK: Towards the Science ofSecurity and Privacy in Machine Learning",
  Papernot et al. (2016)
  [[link](https://arxiv.org/abs/1611.03814)]
  [[pdf](https://arxiv.org/pdf/1611.03814.pdf)]
- "Robustness and generalization", Xu & Manor (2012)
  [[link](https://link.springer.com/article/10.1007/s10994-011-5268-1)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/s10994-011-5268-1.pdf)]
  [[doi](https://doi.org/10.1007/s10994-011-5268-1)]

### 2.7. Cyber-Physical Systems

- "Verification Approaches for Learning-Enabled Autonomous Cyber-Physical
  Systems",
  Tran et al. (2020)
  [[link](https://ieeexplore.ieee.org/document/9165805)]
  [[pdf](https://www.researchgate.net/publication/328091692_Verification_for_Machine_Learning_Autonomy_and_Neural_Networks_Survey)]
  [[doi](https://doi.org/10.1109/MDAT.2020.3015712)]
- "Vulnerabilities and safety assurance methods in Cyber-Physical Systems:
  A comprehensive review.", <!-- Period at end is part of the title somehow -->
  Bolbot et al. (2019)
  [[link](https://www.sciencedirect.com/science/article/abs/pii/S0951832018302709)]
  [[pdf](https://strathprints.strath.ac.uk/65628/1/Bolbot_etal_RESS2018_Vulnerabilities_and_safety_assurance_methods_in_Cyber_Physical.pdf)]
  [[doi](https://doi.org/10.1016/j.ress.2018.09.004)]
- "Verising: verifying safety properties of hybrid systems with neural network
  controllers",
  Ivanov et al. (2019)
  [[link](https://dl.acm.org/doi/abs/10.1145/3302504.3311806)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3302504.3311806)]
  [[doi](https://doi.org/10.1145/3302504.3311806)]
- "The Logical Path to Autonomous Cyber-Physical Systems",
  Platzer (2019)
  [[link](https://link.springer.com/chapter/10.1007%2F978-3-030-30281-8_2)]
  [[pdf](https://lfcps.org/pub/lpacps.pdf)]
  [[doi](https://doi.org/10.1007/978-3-030-30281-8_2)]
- "Formal Verification of Neural Network Controlled Autonomous Systems",
  Sun et al. (2019)
  [[link](https://dl.acm.org/doi/abs/10.1145/3302504.3311802)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3302504.3311802)]
  [[doi](https://doi.org/10.1145/3302504.3311802)]
- "Safety Verification of Cyber-Physical Systems with Reinforcement Learning
  Control",
  Tran et al. (2019)
  [[link](https://dl.acm.org/doi/abs/10.1145/3358230)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3358230)]
  [[doi](https://doi.org/10.1145/3358230)]
- "A Systematic Mapping Study on the Verification of Cyber-Physical Systems",
  Duan et al. (2018)
  [[link](https://ieeexplore.ieee.org/abstract/document/8472900/)]
  [[pdf](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8472900)]
  [[doi](https://doi.org/10.1109/ACCESS.2018.2872015)]
- "Reasoning about Safety of Learning-Enabled Components in Autonomous
  Cyber-physical Systems",
  Tuncali et al. (2018)
  [[link](https://dl.acm.org/doi/abs/10.1145/3195970.3199852)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3195970.3199852)]
  [[doi](https://doi.org/10.1145/3195970.3199852)]
- "Reachable Set Estimation and Verification for Neural Network Models of
  Nonlinear Dynamic Systems",
  Xiang et al. (2018)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-97301-2_7)]
  [[pdf](https://arxiv.org/pdf/1802.03557)]
  [[doi](https://doi.org/10.1007/978-3-319-97301-2_7)]
- "Work-in-Progress: Testing Autonomous Cyber-Physical Systems using Fuzzing
  Features from Convolutional Neural Networks",
  Raj et al. (2017)
  [[link](https://ieeexplore.ieee.org/abstract/document/8094374)]
  [[pdf](https://dl.acm.org/doi/pdf/10.1145/3125503.3125568)]
  [[doi](https://doi.org/10.1145/3125503.3125568)]
- "Integrating Symbolic and Statistical Methods for TestingIntelligent Systems",
  Ramanathan et al. (2016)
  [[link](https://ieeexplore.ieee.org/abstract/document/7459413)]
  [[pdf](https://past.date-conference.com/proceedings-archive/2016/pdf/0954.pdf)]
- "Modeling and Verifying Intelligent Automotive Cyber-Physical Systems",
  Jha & Sukthankar (2011)
  [[pdf](http://roke.eecs.ucf.edu/pdf/Sukthankar-CPS2011.pdf)]

## 3. Integrated Approaches

### 3.1. Executable Specifications

- "Labor Division with Movable Walls: Composing Executable Specifications with
  Machine Learning and Search (Blue Sky Idea)"
  Harel et al. (2019)
  [[link](https://www.aaai.org/ojs/index.php/AAAI/article/view/5048)]
  [[pdf](https://www.aaai.org/ojs/index.php/AAAI/article/view/5048/4921)]
  [[doi](https://doi.org/10.1609/aaai.v33i01.33019770)]

### 3.2. Cyber-Physical Systems

- "Compositional Falsification of Cyber-Physical Systems with Machine Learning
  Components",
  Dreossi et al. (2019)
  [[link](https://link.springer.com/article/10.1007%2Fs10817-018-09509-5)]
  [[pdf](https://link.springer.com/content/pdf/10.1007/s10817-018-09509-5.pdf)]
  [[doi](https://doi.org/10.1007/s10817-018-09509-5)]
- "Design and verification of Cyber-Physical Systems using TrueTime,
  evolutionary optimization and UPPAAL",
  Balasubramaniyan et al. (2016)
  [[link](https://www.sciencedirect.com/science/article/abs/pii/S0141933116000089)]
  [[doi](https://doi.org/10.1016/j.micpro.2015.12.006)]
- "Towards Learning and Verifying Invariants of Cyber-Physical Systems by
  Code Mutation",
  Chen et al. (2016)
  [[link](https://link.springer.com/chapter/10.1007/978-3-319-48989-6_10)]
  [[pdf](https://arxiv.org/pdf/1609.01491.pdf)]
  [[doi](https://doi.org/10.1007/978-3-319-48989-6_10)]

### 3.3. Pattern Recognition

- "A Formal Methods Approach to Pattern Synthesis in Reaction Diffusion Systems",
  Gol et al. (2014)
  [[link](https://ieeexplore.ieee.org/abstract/document/7039367/)]
  [[pdf](https://arxiv.org/pdf/1409.5671.pdf)]
  [[doi](https://doi.org/10.1109/CDC.2014.7039367)]

## 4. Unsorted Online Sources

### 4.1. Courses

- "Formal Verification Meets Machine Learning",
  Thomas Noll, Seminar in Theoretical CS, Summer Semester 2018, RWTH Aachen
  [[link](https://moves.rwth-aachen.de/teaching/ss-18/fvmml/)]
