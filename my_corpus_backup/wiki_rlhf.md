[Jump to content](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#bodyContent)
Main menu
Main menu
move to sidebar hide
Navigation 
  * [Main page](https://en.wikipedia.org/wiki/Main_Page "Visit the main page \[z\]")
  * [Contents](https://en.wikipedia.org/wiki/Wikipedia:Contents "Guides to browsing Wikipedia")
  * [Current events](https://en.wikipedia.org/wiki/Portal:Current_events "Articles related to current events")
  * [Random article](https://en.wikipedia.org/wiki/Special:Random "Visit a randomly selected article \[x\]")
  * [About Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:About "Learn about Wikipedia and how it works")
  * [Contact us](https://en.wikipedia.org/wiki/Wikipedia:Contact_us "How to contact Wikipedia")


Contribute 
  * [Help](https://en.wikipedia.org/wiki/Help:Contents "Guidance on how to use and edit Wikipedia")
  * [Learn to edit](https://en.wikipedia.org/wiki/Help:Introduction "Learn how to edit Wikipedia")
  * [Community portal](https://en.wikipedia.org/wiki/Wikipedia:Community_portal "The hub for editors")
  * [Recent changes](https://en.wikipedia.org/wiki/Special:RecentChanges "A list of recent changes to Wikipedia \[r\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_upload_wizard "Add images or other media for use on Wikipedia")
  * [Special pages](https://en.wikipedia.org/wiki/Special:SpecialPages "A list of all special pages \[q\]")


[ ![](https://en.wikipedia.org/static/images/icons/enwiki-25.svg) ![Wikipedia](https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg) ![The Free Encyclopedia](https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-tagline-en-25.svg) ](https://en.wikipedia.org/wiki/Main_Page)
[Search ](https://en.wikipedia.org/wiki/Special:Search "Search Wikipedia \[f\]")
Search
Appearance
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Reinforcement+learning+from+human+feedback "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Reinforcement+learning+from+human+feedback "You're encouraged to log in; however, it's not mandatory. \[o\]")


Personal tools
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Reinforcement+learning+from+human+feedback "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Reinforcement+learning+from+human+feedback "You're encouraged to log in; however, it's not mandatory. \[o\]")


## Contents
move to sidebar hide
  * [ (Top) ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
  * [ 1 Background and motivation ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Background_and_motivation)
  * [ 2 Collecting human feedback ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Collecting_human_feedback)
  * [ 3 Applications ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Applications)
  * [ 4 Training ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Training) Toggle Training subsection
    * [ 4.1 Reward model ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Reward_model)
    * [ 4.2 Policy ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Policy)
    * [ 4.3 Proximal policy optimization ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Proximal_policy_optimization)
    * [ 4.4 Mixing pretraining gradients ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Mixing_pretraining_gradients)
  * [ 5 Limitations ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Limitations)
  * [ 6 Alternatives ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Alternatives) Toggle Alternatives subsection
    * [ 6.1 Reinforcement learning from AI feedback ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Reinforcement_learning_from_AI_feedback)
    * [ 6.2 Direct alignment algorithms ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Direct_alignment_algorithms)
      * [ 6.2.1 Direct preference optimization ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Direct_preference_optimization)
      * [ 6.2.2 Identity preference optimization ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Identity_preference_optimization)
      * [ 6.2.3 Kahneman-Tversky optimization ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Kahneman-Tversky_optimization)
  * [ 7 See also ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#See_also)
  * [ 8 References ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#References)
  * [ 9 Further reading ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#Further_reading)


Toggle the table of contents
# Reinforcement learning from human feedback
20 languages
  * [Afrikaans](https://af.wikipedia.org/wiki/Versterkingleer_uit_menslike_terugvoer "Versterkingleer uit menslike terugvoer – Afrikaans")
  * [العربية](https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%AA%D8%B9%D9%84%D9%85_%D8%A7%D9%84%D9%85%D8%B9%D8%B2%D8%B2_%D9%85%D9%86_%D8%B1%D8%AF%D9%88%D8%AF_%D8%A7%D9%84%D9%81%D8%B9%D9%84_%D8%A7%D9%84%D8%A8%D8%B4%D8%B1%D9%8A%D8%A9 "التعلم المعزز من ردود الفعل البشرية – Arabic")
  * [Bosanski](https://bs.wikipedia.org/wiki/Podr%C5%BEano_u%C4%8Denje_na_osnovu_povratnih_informacija_od_ljudi "Podržano učenje na osnovu povratnih informacija od ljudi – Bosnian")
  * [Català](https://ca.wikipedia.org/wiki/Aprenentatge_de_refor%C3%A7_a_partir_de_la_retroalimentaci%C3%B3_humana "Aprenentatge de reforç a partir de la retroalimentació humana – Catalan")
  * [Deutsch](https://de.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback – German")
  * [Español](https://es.wikipedia.org/wiki/Aprendizaje_por_refuerzo_a_partir_de_retroalimentaci%C3%B3n_humana "Aprendizaje por refuerzo a partir de retroalimentación humana – Spanish")
  * [Eesti](https://et.wikipedia.org/wiki/Inimtagasisidest_l%C3%A4htuv_stiimul%C3%B5pe "Inimtagasisidest lähtuv stiimulõpe – Estonian")
  * [فارسی](https://fa.wikipedia.org/wiki/%DB%8C%D8%A7%D8%AF%DA%AF%DB%8C%D8%B1%DB%8C_%D8%AA%D9%82%D9%88%DB%8C%D8%AA%DB%8C_%D8%A7%D8%B2_%D8%A8%D8%A7%D8%B2%D8%AE%D9%88%D8%B1%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86%DB%8C "یادگیری تقویتی از بازخورد انسانی – Persian")
  * [Français](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement_%C3%A0_partir_de_r%C3%A9troaction_humaine "Apprentissage par renforcement à partir de rétroaction humaine – French")
  * [Gaeilge](https://ga.wikipedia.org/wiki/Foghlaim_atreisithe_%C3%B3_aiseolas_%C3%B3n_duine "Foghlaim atreisithe ó aiseolas ón duine – Irish")
  * [日本語](https://ja.wikipedia.org/wiki/%E4%BA%BA%E9%96%93%E3%81%AE%E3%83%95%E3%82%A3%E3%83%BC%E3%83%89%E3%83%90%E3%83%83%E3%82%AF%E3%81%AB%E3%82%88%E3%82%8B%E5%BC%B7%E5%8C%96%E5%AD%A6%E7%BF%92 "人間のフィードバックによる強化学習 – Japanese")
  * [한국어](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B0%84_%ED%94%BC%EB%93%9C%EB%B0%B1%EC%9D%84_%ED%86%B5%ED%95%9C_%EA%B0%95%ED%99%94_%ED%95%99%EC%8A%B5 "인간 피드백을 통한 강화 학습 – Korean")
  * [Polski](https://pl.wikipedia.org/wiki/RLHF "RLHF – Polish")
  * [Português](https://pt.wikipedia.org/wiki/Aprendizado_por_refor%C3%A7o_com_feedback_humano "Aprendizado por reforço com feedback humano – Portuguese")
  * [Русский](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81_%D0%BF%D0%BE%D0%B4%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC_%D0%BD%D0%B0_%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B5_%D0%BE%D1%82%D0%B7%D1%8B%D0%B2%D0%BE%D0%B2_%D0%BB%D1%8E%D0%B4%D0%B5%D0%B9 "Обучение с подкреплением на основе отзывов людей – Russian")
  * [Српски / srpski](https://sr.wikipedia.org/wiki/%D0%A3%D1%87%D0%B5%D1%9A%D0%B5_%D0%BF%D0%BE%D1%82%D0%BA%D1%80%D0%B5%D0%BF%D1%99%D0%B5%D1%9A%D0%B5%D0%BC_%D0%B8%D0%B7_%D1%99%D1%83%D0%B4%D1%81%D0%BA%D0%B8%D1%85_%D0%BF%D0%BE%D0%B2%D1%80%D0%B0%D1%82%D0%BD%D0%B8%D1%85_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%98%D0%B0 "Учење поткрепљењем из људских повратних информација – Serbian")
  * [தமிழ்](https://ta.wikipedia.org/wiki/%E0%AE%AE%E0%AE%A9%E0%AE%BF%E0%AE%A4%E0%AE%AA%E0%AF%8D_%E0%AE%AA%E0%AE%BF%E0%AE%A9%E0%AF%8D%E0%AE%A9%E0%AF%82%E0%AE%9F%E0%AF%8D%E0%AE%9F_%E0%AE%B5%E0%AE%B4%E0%AE%BF_%E0%AE%B5%E0%AE%B2%E0%AF%81%E0%AE%B5%E0%AF%82%E0%AE%9F%E0%AF%8D%E0%AE%9F%E0%AE%B2%E0%AF%8D_%E0%AE%95%E0%AE%B1%E0%AF%8D%E0%AE%B1%E0%AE%B2%E0%AF%8D "மனிதப் பின்னூட்ட வழி வலுவூட்டல் கற்றல் – Tamil")
  * [Українська](https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B2%D1%87%D0%B0%D0%BD%D0%BD%D1%8F_%D0%B7_%D0%BF%D1%96%D0%B4%D0%BA%D1%80%D1%96%D0%BF%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F%D0%BC_%D0%BB%D1%8E%D0%B4%D1%81%D1%8C%D0%BA%D0%B8%D0%BC_%D0%B7%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%BD%D0%B8%D0%BC_%D0%B7%D0%B2%27%D1%8F%D0%B7%D0%BA%D0%BE%D0%BC "Навчання з підкріпленням людським зворотним зв'язком – Ukrainian")
  * [Tiếng Việt](https://vi.wikipedia.org/wiki/H%E1%BB%8Dc_t%C4%83ng_c%C6%B0%E1%BB%9Dng_t%E1%BB%AB_ph%E1%BA%A3n_h%E1%BB%93i_c%E1%BB%A7a_con_ng%C6%B0%E1%BB%9Di "Học tăng cường từ phản hồi của con người – Vietnamese")
  * [中文](https://zh.wikipedia.org/wiki/%E5%9F%BA%E4%BA%8E%E4%BA%BA%E7%B1%BB%E5%8F%8D%E9%A6%88%E7%9A%84%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0 "基于人类反馈的强化学习 – Chinese")


[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q115570683#sitelinks-wikipedia "Edit interlanguage links")
  * [Article](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "View the content page \[c\]")
  * [Talk](https://en.wikipedia.org/wiki/Talk:Reinforcement_learning_from_human_feedback "Discuss improvements to the content page \[t\]")


English
  * [Read](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
  * [Edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=history "Past revisions of this page \[h\]")


Tools
Tools
move to sidebar hide
Actions 
  * [Read](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
  * [Edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=history)


General 
  * [What links here](https://en.wikipedia.org/wiki/Special:WhatLinksHere/Reinforcement_learning_from_human_feedback "List of all English Wikipedia pages containing links to this page \[j\]")
  * [Related changes](https://en.wikipedia.org/wiki/Special:RecentChangesLinked/Reinforcement_learning_from_human_feedback "Recent changes in pages linked from this page \[k\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files \[u\]")
  * [Permanent link](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&oldid=1354240262 "Permanent link to this revision of this page")
  * [Page information](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=info "More information about this page")
  * [Cite this page](https://en.wikipedia.org/w/index.php?title=Special:CiteThisPage&page=Reinforcement_learning_from_human_feedback&id=1354240262&wpFormIdentifier=titleform "Information on how to cite this page")
  * [Get shortened URL](https://en.wikipedia.org/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FReinforcement_learning_from_human_feedback)


Print/export 
  * [Download as PDF](https://en.wikipedia.org/w/index.php?title=Special:DownloadAsPdf&page=Reinforcement_learning_from_human_feedback&action=show-download-screen "Download this page as a PDF file")
  * [Printable version](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&printable=yes "Printable version of this page \[p\]")


In other projects 
  * [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q115570683 "Structured data on this page hosted by Wikidata \[g\]")


Appearance
move to sidebar hide
[![This is a good article. Click here for more information.](https://upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/20px-Symbol_support_vote.svg.png)](https://en.wikipedia.org/wiki/Wikipedia:Good_articles* "This is a good article. Click here for more information.")
From Wikipedia, the free encyclopedia
Machine learning technique
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/RLHF_diagram.svg/500px-RLHF_diagram.svg.png)](https://en.wikipedia.org/wiki/File:RLHF_diagram.svg)High-level overview of reinforcement learning from human feedback  
| Part of a series on |  
| --- |  
|  [Machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning")  
and [data mining](https://en.wikipedia.org/wiki/Data_mining "Data mining")  |  
|  Paradigms
  * [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning")
  * [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning "Unsupervised learning")
  * [Semi-supervised learning](https://en.wikipedia.org/wiki/Semi-supervised_learning "Semi-supervised learning")
  * [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning")
  * [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning")
  * [Meta-learning](https://en.wikipedia.org/wiki/Meta-learning_\(computer_science\) "Meta-learning \(computer science\)")
  * [Online learning](https://en.wikipedia.org/wiki/Online_machine_learning "Online machine learning")
  * [Batch learning](https://en.wikipedia.org/wiki/Batch_learning "Batch learning")
  * [Curriculum learning](https://en.wikipedia.org/wiki/Curriculum_learning "Curriculum learning")
  * [Rule-based learning](https://en.wikipedia.org/wiki/Rule-based_machine_learning "Rule-based machine learning")
  * [Neuro-symbolic AI](https://en.wikipedia.org/wiki/Neuro-symbolic_AI "Neuro-symbolic AI")
  * [Neuromorphic engineering](https://en.wikipedia.org/wiki/Neuromorphic_engineering "Neuromorphic engineering")
  * [Quantum machine learning](https://en.wikipedia.org/wiki/Quantum_machine_learning "Quantum machine learning")

 |  
|  Problems
  * [Classification](https://en.wikipedia.org/wiki/Statistical_classification "Statistical classification")
  * [Generative modeling](https://en.wikipedia.org/wiki/Generative_model "Generative model")
  * [Regression](https://en.wikipedia.org/wiki/Regression_analysis "Regression analysis")
  * [Clustering](https://en.wikipedia.org/wiki/Cluster_analysis "Cluster analysis")
  * [Dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction "Dimensionality reduction")
  * [Density estimation](https://en.wikipedia.org/wiki/Density_estimation "Density estimation")
  * [Anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection "Anomaly detection")
  * [Data cleaning](https://en.wikipedia.org/wiki/Data_cleaning "Data cleaning")
  * [AutoML](https://en.wikipedia.org/wiki/Automated_machine_learning "Automated machine learning")
  * [Association rules](https://en.wikipedia.org/wiki/Association_rule_learning "Association rule learning")
  * [Semantic analysis](https://en.wikipedia.org/wiki/Semantic_analysis_\(machine_learning\) "Semantic analysis \(machine learning\)")
  * [Structured prediction](https://en.wikipedia.org/wiki/Structured_prediction "Structured prediction")
  * [Feature engineering](https://en.wikipedia.org/wiki/Feature_engineering "Feature engineering")
  * [Feature learning](https://en.wikipedia.org/wiki/Feature_learning "Feature learning")
  * [Learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank "Learning to rank")
  * [Grammar induction](https://en.wikipedia.org/wiki/Grammar_induction "Grammar induction")
  * [Ontology learning](https://en.wikipedia.org/wiki/Ontology_learning "Ontology learning")
  * [Multimodal learning](https://en.wikipedia.org/wiki/Multimodal_learning "Multimodal learning")

 |  
|  [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning")  
(**[classification](https://en.wikipedia.org/wiki/Statistical_classification "Statistical classification")** • **[regression](https://en.wikipedia.org/wiki/Regression_analysis "Regression analysis")**)
  * [Apprenticeship learning](https://en.wikipedia.org/wiki/Apprenticeship_learning "Apprenticeship learning")
  * [Decision trees](https://en.wikipedia.org/wiki/Decision_tree_learning "Decision tree learning")
  * [Ensembles](https://en.wikipedia.org/wiki/Ensemble_learning "Ensemble learning")
    * [Bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating "Bootstrap aggregating")
    * [Boosting](https://en.wikipedia.org/wiki/Boosting_\(machine_learning\) "Boosting \(machine learning\)")
    * [Random forest](https://en.wikipedia.org/wiki/Random_forest "Random forest")
  * [_k_ -NN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm "K-nearest neighbors algorithm")
  * [Linear regression](https://en.wikipedia.org/wiki/Linear_regression "Linear regression")
  * [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier "Naive Bayes classifier")
  * [Artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network "Artificial neural network")
  * [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression "Logistic regression")
  * [Perceptron](https://en.wikipedia.org/wiki/Perceptron "Perceptron")
  * [Relevance vector machine (RVM)](https://en.wikipedia.org/wiki/Relevance_vector_machine "Relevance vector machine")
  * [Support vector machine (SVM)](https://en.wikipedia.org/wiki/Support_vector_machine "Support vector machine")

 |  
|  [Clustering](https://en.wikipedia.org/wiki/Cluster_analysis "Cluster analysis")
  * [BIRCH](https://en.wikipedia.org/wiki/BIRCH "BIRCH")
  * [CURE](https://en.wikipedia.org/wiki/CURE_algorithm "CURE algorithm")
  * [Hierarchical](https://en.wikipedia.org/wiki/Hierarchical_clustering "Hierarchical clustering")
  * [_k_ -means](https://en.wikipedia.org/wiki/K-means_clustering "K-means clustering")
  * [Fuzzy](https://en.wikipedia.org/wiki/Fuzzy_clustering "Fuzzy clustering")
  * [Expectation–maximization (EM)](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm "Expectation–maximization algorithm")
  *   
[DBSCAN](https://en.wikipedia.org/wiki/DBSCAN "DBSCAN")
  * [OPTICS](https://en.wikipedia.org/wiki/OPTICS_algorithm "OPTICS algorithm")
  * [Mean shift](https://en.wikipedia.org/wiki/Mean_shift "Mean shift")

 |  
|  [Dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction "Dimensionality reduction")
  * [Factor analysis](https://en.wikipedia.org/wiki/Factor_analysis "Factor analysis")
  * [CCA](https://en.wikipedia.org/wiki/Canonical_correlation "Canonical correlation")
  * [ICA](https://en.wikipedia.org/wiki/Independent_component_analysis "Independent component analysis")
  * [LDA](https://en.wikipedia.org/wiki/Linear_discriminant_analysis "Linear discriminant analysis")
  * [NMF](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization "Non-negative matrix factorization")
  * [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis "Principal component analysis")
  * [PGD](https://en.wikipedia.org/wiki/Proper_generalized_decomposition "Proper generalized decomposition")
  * [t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding "T-distributed stochastic neighbor embedding")
  * [SDL](https://en.wikipedia.org/wiki/Sparse_dictionary_learning "Sparse dictionary learning")

 |  
|  [Structured prediction](https://en.wikipedia.org/wiki/Structured_prediction "Structured prediction")
  * [Graphical models](https://en.wikipedia.org/wiki/Graphical_model "Graphical model")
    * [Bayes net](https://en.wikipedia.org/wiki/Bayesian_network "Bayesian network")
    * [Conditional random field](https://en.wikipedia.org/wiki/Conditional_random_field "Conditional random field")
    * [Hidden Markov](https://en.wikipedia.org/wiki/Hidden_Markov_model "Hidden Markov model")

 |  
|  [Anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection "Anomaly detection")
  * [RANSAC](https://en.wikipedia.org/wiki/Random_sample_consensus "Random sample consensus")
  * [_k_ -NN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm "K-nearest neighbors algorithm")
  * [Local outlier factor](https://en.wikipedia.org/wiki/Local_outlier_factor "Local outlier factor")
  * [Isolation forest](https://en.wikipedia.org/wiki/Isolation_forest "Isolation forest")

 |  
|  [Neural networks](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\) "Neural network \(machine learning\)")
  * [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder "Autoencoder")
  * [Deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning")
  * [Feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network "Feedforward neural network")
  * [Recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network "Recurrent neural network")
    * [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory "Long short-term memory")
    * [GRU](https://en.wikipedia.org/wiki/Gated_recurrent_unit "Gated recurrent unit")
    * [ESN](https://en.wikipedia.org/wiki/Echo_state_network "Echo state network")
    * [reservoir computing](https://en.wikipedia.org/wiki/Reservoir_computing "Reservoir computing")
  * [Boltzmann machine](https://en.wikipedia.org/wiki/Boltzmann_machine "Boltzmann machine")
    * [Restricted](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine "Restricted Boltzmann machine")
  * [GAN](https://en.wikipedia.org/wiki/Generative_adversarial_network "Generative adversarial network")
  * [Diffusion model](https://en.wikipedia.org/wiki/Diffusion_model "Diffusion model")
  * [SOM](https://en.wikipedia.org/wiki/Self-organizing_map "Self-organizing map")
  * [Convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network "Convolutional neural network")
    * [U-Net](https://en.wikipedia.org/wiki/U-Net "U-Net")
    * [LeNet](https://en.wikipedia.org/wiki/LeNet "LeNet")
    * [AlexNet](https://en.wikipedia.org/wiki/AlexNet "AlexNet")
    * [DeepDream](https://en.wikipedia.org/wiki/DeepDream "DeepDream")
  * [Neural field](https://en.wikipedia.org/wiki/Neural_field "Neural field")
    * [Neural radiance field](https://en.wikipedia.org/wiki/Neural_radiance_field "Neural radiance field")
    * [Physics-informed neural networks](https://en.wikipedia.org/wiki/Physics-informed_neural_networks "Physics-informed neural networks")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\) "Transformer \(deep learning architecture\)")
    * [Vision](https://en.wikipedia.org/wiki/Vision_transformer "Vision transformer")
  * [Mamba](https://en.wikipedia.org/wiki/Mamba_\(deep_learning_architecture\) "Mamba \(deep learning architecture\)")
  * [Spiking neural network](https://en.wikipedia.org/wiki/Spiking_neural_network "Spiking neural network")
  * [Memtransistor](https://en.wikipedia.org/wiki/Memtransistor "Memtransistor")
  * [Electrochemical RAM](https://en.wikipedia.org/wiki/Electrochemical_RAM "Electrochemical RAM") (ECRAM)

 |  
|  [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning")
  * [Q-learning](https://en.wikipedia.org/wiki/Q-learning "Q-learning")
  * [Policy gradient](https://en.wikipedia.org/wiki/Policy_gradient_method "Policy gradient method")
  * [SARSA](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action "State–action–reward–state–action")
  * [Temporal difference (TD)](https://en.wikipedia.org/wiki/Temporal_difference_learning "Temporal difference learning")
  * [Multi-agent](https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning "Multi-agent reinforcement learning")
    * [Self-play](https://en.wikipedia.org/wiki/Self-play_\(reinforcement_learning_technique\) "Self-play \(reinforcement learning technique\)")

 |  
|  Learning with humans
  * [Active learning](https://en.wikipedia.org/wiki/Active_learning_\(machine_learning\) "Active learning \(machine learning\)")
  * [Crowdsourcing](https://en.wikipedia.org/wiki/Crowdsourcing "Crowdsourcing")
  * [Human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop "Human-in-the-loop")
  * [Mechanistic interpretability](https://en.wikipedia.org/wiki/Mechanistic_interpretability "Mechanistic interpretability")
  * RLHF

 |  
|  Model diagnostics
  * [Coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination "Coefficient of determination")
  * [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix "Confusion matrix")
  * [Learning curve](https://en.wikipedia.org/wiki/Learning_curve_\(machine_learning\) "Learning curve \(machine learning\)")
  * [ROC curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic "Receiver operating characteristic")

 |  
|  Mathematical foundations
  * [Kernel machines](https://en.wikipedia.org/wiki/Kernel_machines "Kernel machines")
  * [Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff "Bias–variance tradeoff")
  * [Computational learning theory](https://en.wikipedia.org/wiki/Computational_learning_theory "Computational learning theory")
  * [Empirical risk minimization](https://en.wikipedia.org/wiki/Empirical_risk_minimization "Empirical risk minimization")
  * [Occam learning](https://en.wikipedia.org/wiki/Occam_learning "Occam learning")
  * [PAC learning](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning "Probably approximately correct learning")
  * [Statistical learning](https://en.wikipedia.org/wiki/Statistical_learning_theory "Statistical learning theory")
  * [VC theory](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory "Vapnik–Chervonenkis theory")
  * [Topological deep learning](https://en.wikipedia.org/wiki/Topological_deep_learning "Topological deep learning")

 |  
|  Journals and conferences
  * [AAAI](https://en.wikipedia.org/wiki/AAAI_Conference_on_Artificial_Intelligence "AAAI Conference on Artificial Intelligence")
  * [CVPR](https://en.wikipedia.org/wiki/Conference_on_Computer_Vision_and_Pattern_Recognition "Conference on Computer Vision and Pattern Recognition")
  * [ECCV](https://en.wikipedia.org/wiki/European_Conference_on_Computer_Vision "European Conference on Computer Vision")
  * [ECML PKDD](https://en.wikipedia.org/wiki/ECML_PKDD "ECML PKDD")
  * [EMNLP](https://en.wikipedia.org/wiki/Empirical_Methods_in_Natural_Language_Processing "Empirical Methods in Natural Language Processing")
  * [ICCV](https://en.wikipedia.org/wiki/International_Conference_on_Computer_Vision "International Conference on Computer Vision")
  * [NeurIPS](https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems "Conference on Neural Information Processing Systems")
  * [ICML](https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning "International Conference on Machine Learning")
  * [ICLR](https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations "International Conference on Learning Representations")
  * [IJCAI](https://en.wikipedia.org/wiki/International_Joint_Conference_on_Artificial_Intelligence "International Joint Conference on Artificial Intelligence")
  * [ML](https://en.wikipedia.org/wiki/Machine_Learning_\(journal\) "Machine Learning \(journal\)")
  * [JMLR](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research "Journal of Machine Learning Research")

 |  
|  Related articles
  * [Glossary of artificial intelligence](https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence "Glossary of artificial intelligence")
  * [List of datasets for machine-learning research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research "List of datasets for machine-learning research")
    * [List of datasets in computer vision and image processing](https://en.wikipedia.org/wiki/List_of_datasets_in_computer_vision_and_image_processing "List of datasets in computer vision and image processing")
  * [Outline of machine learning](https://en.wikipedia.org/wiki/Outline_of_machine_learning "Outline of machine learning")

 |  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Machine_learning "Template:Machine learning")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Machine_learning "Template talk:Machine learning")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Machine_learning "Special:EditPage/Template:Machine learning")

 |  
In [machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning"), **reinforcement learning from human feedback** (**RLHF**) is a technique to [align](https://en.wikipedia.org/wiki/AI_alignment "AI alignment") an [intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent "Intelligent agent") with human [preferences](https://en.wikipedia.org/wiki/Preference "Preference"). It involves training a [reward model](https://en.wikipedia.org/w/index.php?title=Reward_model&action=edit&redlink=1 "Reward model \(page does not exist\)") to represent preferences, which can then be used to train other models through [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning").[[1]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-1)
In classical reinforcement learning, an intelligent agent's goal is to learn a function that guides its behavior, called a [policy](https://en.wikipedia.org/wiki/Reinforcement_learning#Policy "Reinforcement learning").[[2]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-2) The function is iteratively optimized to increase the reward signal derived from the agent's task performance.[[3]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-3) However, explicitly defining a reward function that accurately approximates human preferences is challenging. Therefore, RLHF seeks to train a "reward model" directly from human [feedback](https://en.wikipedia.org/wiki/Feedback "Feedback").[[4]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-ziegler-4) The reward model is first trained in a [supervised](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning") manner to predict if a response to a given prompt is good (high reward) or bad (low reward) based on ranking data collected from human [annotators](https://en.wikipedia.org/wiki/Labeled_data "Labeled data"). This model then serves as a reward function to improve an agent's policy through an [optimization algorithm](https://en.wikipedia.org/wiki/Optimization_algorithm "Optimization algorithm") like [proximal policy optimization](https://en.wikipedia.org/wiki/Proximal_policy_optimization "Proximal policy optimization").[[5]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-huggingface-5)[[6]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-6)[[7]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-7)
RLHF has applications in various domains in machine learning, including [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") tasks such as [text summarization](https://en.wikipedia.org/wiki/Text_summarization "Text summarization") and [conversational agents](https://en.wikipedia.org/wiki/Conversational_agents "Conversational agents"), [computer vision](https://en.wikipedia.org/wiki/Computer_vision "Computer vision") tasks like [text-to-image models](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model"), and the development of [video game bots](https://en.wikipedia.org/wiki/Video_game_bot "Video game bot"). While RLHF is an effective method of training models to act better in accordance with human preferences, it also faces challenges due to the way the human preference data is collected. Though RLHF does not require massive amounts of data to improve performance, sourcing high-quality preference data is still an expensive process. Furthermore, if the data is not carefully collected from a representative [sample](https://en.wikipedia.org/wiki/Sampling_\(statistics\) "Sampling \(statistics\)"), the resulting model may exhibit unwanted [biases](https://en.wikipedia.org/wiki/Algorithmic_bias "Algorithmic bias"). 
## Background and motivation
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=1 "Edit section: Background and motivation")]
Optimizing a model based on human feedback is desirable when a task is difficult to specify yet easy to judge.[[8]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openai-8) For example, one may want to train a model to generate [safe](https://en.wikipedia.org/wiki/AI_safety "AI safety") text that is both helpful and harmless (such as lacking [bias](https://en.wikipedia.org/wiki/Algorithmic_bias "Algorithmic bias"), toxicity, or otherwise harmful content). Asking humans to manually create examples of harmless and harmful text would be difficult and time-consuming. However, humans are adept at swiftly assessing and comparing the harmfulness of different AI-generated text. Therefore, a more practical objective would be to allow the model to use this type of human feedback to improve its text generation.[[9]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-:0-9)
Despite the clear benefits of incorporating human feedback in training models, prior efforts—including some that leverage [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning") (RL)—have encountered significant challenges. Most attempts were either narrow and difficult to generalize, breaking down on more complex tasks,[[10]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-10)[[11]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-11)[[12]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-12)[[13]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-13) or they faced difficulties learning from sparse (lacking specific information and relating to large amounts of text at a time) or noisy (inconsistently rewarding similar outputs) reward functions.[[14]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-14)[[15]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-15)
RLHF was not the first successful method of using human feedback for reinforcement learning, but it is one of the most widely used. The foundation for RLHF was introduced as an attempt to create a general algorithm for learning from a practical amount of human feedback.[[8]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openai-8)[[5]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-huggingface-5) The algorithm as used today was introduced by [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") in a paper on enhancing text continuation or summarization based on human feedback, and it began to gain popularity when the same method was reused in their paper on [InstructGPT](https://en.wikipedia.org/wiki/InstructGPT "InstructGPT").[[4]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-ziegler-4)[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16)[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17) RLHF has also been shown to improve the [robustness](https://en.wikipedia.org/wiki/Robust_optimization "Robust optimization") of RL agents and their capacity for [exploration](https://en.wikipedia.org/wiki/Exploration_\(reinforcement_learning\) "Exploration \(reinforcement learning\)"), which results in an optimization process more adept at handling [uncertainty](https://en.wikipedia.org/wiki/Uncertainty "Uncertainty") and efficiently exploring its environment in search of the highest reward.[[18]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-18)
## Collecting human feedback
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=2 "Edit section: Collecting human feedback")]
Human feedback is commonly collected by prompting humans to rank instances of the agent's behavior.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)[[19]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-ars-19)[[20]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-20) These rankings can then be used to score outputs, for example, using the [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system "Elo rating system"), which is an algorithm for calculating the relative skill levels of players in a game based only on the outcome of each game.[[5]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-huggingface-5) While ranking outputs is the most widely adopted form of feedback, recent research has explored other forms, such as numerical feedback, natural language feedback, and prompting for direct edits to the model's output.[[21]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-21)
One initial motivation of RLHF was that it requires relatively small amounts of comparison data to be effective.[[8]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openai-8) It has been shown that a small amount of data can lead to comparable results to a larger amount. In addition, increasing the amount of data tends to be less effective than proportionally increasing the size of the reward model.[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16) Nevertheless, a larger and more diverse amount of data can be crucial for tasks where it is important to avoid [bias](https://en.wikipedia.org/wiki/Algorithmic_bias "Algorithmic bias") from a partially [representative](https://en.wikipedia.org/wiki/Representative_sample "Representative sample") group of annotators.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)
When learning from human feedback through [pairwise comparison](https://en.wikipedia.org/wiki/Pairwise_comparison_\(psychology\) "Pairwise comparison \(psychology\)") under the [Bradley–Terry–Luce](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry%E2%80%93Luce "Bradley–Terry–Luce") model (or the [Plackett–Luce](https://en.wikipedia.org/wiki/Discrete_choice "Discrete choice") model for K-wise comparisons over more than two comparisons), the [maximum likelihood estimator](https://en.wikipedia.org/wiki/Maximum_likelihood_estimator "Maximum likelihood estimator") (MLE) for linear reward functions has been shown to [converge](https://en.wikipedia.org/wiki/Convergent_series "Convergent series") if the comparison data is generated under a well-specified [linear model](https://en.wikipedia.org/wiki/Linear_model "Linear model"). This implies that, under certain conditions, if a model is trained to decide which choices people would prefer between pairs (or groups) of choices, it will necessarily improve at predicting future preferences. This improvement is expected as long as the comparisons it learns from are based on a consistent and simple rule.[[22]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-xiejiang-22)[[23]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-pacchiano-23)
Both offline data collection models, where the model is learning by interacting with a static dataset and updating its policy in batches, as well as online data collection models, where the model directly interacts with the dynamic environment and updates its policy immediately, have been mathematically studied proving sample complexity bounds for RLHF under different feedback models.[[22]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-xiejiang-22)[[24]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-zhujordan-24)
In the offline data collection model, when the objective is policy training, a pessimistic MLE that incorporates a lower [confidence bound](https://en.wikipedia.org/wiki/Confidence_bound "Confidence bound") as the reward estimate is most effective. Moreover, when applicable, it has been shown that considering K-wise comparisons directly is [asymptotically more efficient](https://en.wikipedia.org/wiki/Efficiency_\(statistics\)#Asymptotic_efficiency "Efficiency \(statistics\)") than converting them into pairwise comparisons for prediction purposes.[[24]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-zhujordan-24)[[25]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-25)[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)
In the online scenario, when human feedback is collected through pairwise comparisons under the Bradley–Terry–Luce model and the objective is to minimize the algorithm's [regret](https://en.wikipedia.org/wiki/Regret_\(decision_theory\) "Regret \(decision theory\)") (the difference in performance compared to an optimal agent), it has been shown that an optimistic MLE that incorporates an upper [confidence bound](https://en.wikipedia.org/wiki/Confidence_bound "Confidence bound") as the reward estimate can be used to design sample efficient algorithms (meaning that they require relatively little training data). A key challenge in RLHF when learning from pairwise (or dueling) comparisons is associated with the [non-Markovian](https://en.wikipedia.org/wiki/Markov_property "Markov property") nature of its optimal policies. Unlike simpler scenarios where the optimal strategy does [not require memory](https://en.wikipedia.org/wiki/Memoryless "Memoryless") of past actions, in RLHF, the best course of action often depends on previous events and decisions, making the strategy inherently memory-dependent.[[23]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-pacchiano-23)
## Applications
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=3 "Edit section: Applications")]
RLHF has been applied to various domains of [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") (NLP), such as conversational agents, text summarization, and natural language understanding.[[26]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-26)[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16) Ordinary reinforcement learning, in which agents learn from their actions based on a predefined "reward function", is difficult to apply to NLP tasks because the rewards tend to be difficult to define or measure, especially when dealing with complex tasks that involve human values or preferences.[[8]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openai-8) RLHF can steer NLP models, in particular [language models](https://en.wikipedia.org/wiki/Language_model "Language model"), to provide answers that [align](https://en.wikipedia.org/wiki/AI_alignment "AI alignment") with human preferences with regard to such tasks by capturing their preferences beforehand in the reward model. This results in a model capable of generating more relevant responses and rejecting inappropriate or irrelevant queries.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)[[27]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-27) Some notable examples of RLHF-trained language models are [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI")'s [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT") (and its predecessor [InstructGPT](https://en.wikipedia.org/wiki/InstructGPT "InstructGPT")),[[19]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-ars-19)[[28]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-28)[[29]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-29) [DeepMind](https://en.wikipedia.org/wiki/DeepMind "DeepMind")'s [Sparrow](https://en.wikipedia.org/wiki/Sparrow_\(chatbot\) "Sparrow \(chatbot\)"),[[30]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-30)[[31]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-31)[[32]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-32) [Google](https://en.wikipedia.org/wiki/Google "Google")'s [Gemini](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini \(language model\)"),[[33]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-33) and [Anthropic](https://en.wikipedia.org/wiki/Anthropic "Anthropic")'s [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\) "Claude \(language model\)").[[34]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-34)
In computer vision, RLHF has also been used to align [text-to-image models](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model"). Studies that successfully used RLHF for this goal have noted that the use of [KL regularization](https://en.wikipedia.org/wiki/KL_divergence "KL divergence") in RLHF, which aims to prevent the learned policy from straying too far from the unaligned model, helped to stabilize the training process by reducing overfitting to the reward model. The final image outputs from models trained with KL regularization were noted to be of significantly higher quality than those trained without.[[35]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-35)[[36]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-36) Other methods tried to incorporate the feedback through more direct training—based on maximizing the reward without the use of reinforcement learning—but conceded that an RLHF-based approach would likely perform better due to the online sample generation used in RLHF during updates as well as the aforementioned KL regularization over the prior model, which mitigates [overfitting](https://en.wikipedia.org/wiki/Overfitting "Overfitting") to the reward function.[[37]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-37)
RLHF was initially applied to other areas, such as the development of [video game bots](https://en.wikipedia.org/wiki/Video_game_bot "Video game bot") and tasks in [simulated robotics](https://en.wikipedia.org/wiki/Robotics_simulator "Robotics simulator"). For example, OpenAI and DeepMind trained agents to play [Atari](https://en.wikipedia.org/wiki/Atari "Atari") games based on human preferences. In classical RL-based training of such bots, the reward function is simply correlated to how well the agent is performing in the game, usually using metrics like the in-game [score](https://en.wikipedia.org/wiki/Score_\(game\) "Score \(game\)"). In comparison, in RLHF, a human is periodically presented with two clips of the agent's behavior in the game and must decide which one _looks_ better. This approach can teach agents to perform at a competitive level without ever having access to their score. In fact, it was shown that RLHF can sometimes lead to superior performance over RL with score metrics because the human's preferences can contain more useful information than performance-based metrics.[[8]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openai-8)[[38]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-38) The agents achieved strong performance in many of the environments tested, often surpassing human performance.[[39]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-39)
## Training
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=4 "Edit section: Training")]
In RLHF, two different models are trained: a reward model and a [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning") policy. The reward model learns to determine what behavior is desirable based on human feedback, while the policy is guided by the reward model to determine the agent's actions. Both models are commonly initialized using a pre-trained [autoregressive](https://en.wikipedia.org/wiki/Autoregressive "Autoregressive") [language model](https://en.wikipedia.org/wiki/Language_model "Language model"). This model is then customarily trained in a [supervised](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning") manner on a relatively small dataset of pairs of prompts to an assistant and their accompanying responses, written by human annotators. 
### Reward model
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=5 "Edit section: Reward model")]
The **reward model** is a function that takes a [string](https://en.wikipedia.org/wiki/String_\(computer_science\) "String \(computer science\)") (piece of text) as input, and produces a single number, which is the "reward".[[40]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-40)
It is usually initialized with a pre-trained model, as this initializes it with an understanding of language and focuses training explicitly on learning human preferences. In addition to being used to initialize the reward model and the RL policy, the model is then also used to sample data to be compared by annotators.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16)
The reward model is then trained by replacing the final layer of the previous model with a randomly initialized [regression](https://en.wikipedia.org/wiki/Regression_analysis "Regression analysis") head. This change shifts the model from its original [classification](https://en.wikipedia.org/wiki/Statistical_classification "Statistical classification") task over its vocabulary to simply outputting a number corresponding to the score of any given prompt and response. This model is trained on the human preference comparison data collected earlier from the supervised model. In particular, it is trained to [minimize](https://en.wikipedia.org/wiki/Mathematical_optimization "Mathematical optimization") the following [cross-entropy](https://en.wikipedia.org/wiki/Cross-entropy "Cross-entropy") loss function: L ( θ ) = − 1 ( K 2 ) E ( x , y w , y l ) [ log ⁡ ( σ ( r θ ( x , y w ) − r θ ( x , y l ) ) ) ] = − 1 ( K 2 ) E ( x , y w , y l ) log ⁡ [ e r θ ( x , y w ) e r θ ( x , y w ) + e r θ ( x , y l ) ] {\displaystyle {\mathcal {L}}(\theta )=-{\frac {1}{K \choose 2}}E_{(x,y_{w},y_{l})}[\log(\sigma (r_{\theta }(x,y_{w})-r_{\theta }(x,y_{l})))]=-{\frac {1}{K \choose 2}}E_{(x,y_{w},y_{l})}\log \left[{\frac {e^{r_{\theta }(x,y_{w})}}{e^{r_{\theta }(x,y_{w})}+e^{r_{\theta }(x,y_{l})}}}\right]} ![{\\displaystyle {\\mathcal {L}}\(\\theta \)=-{\\frac {1}{K \\choose 2}}E_{\(x,y_{w},y_{l}\)}\[\\log\(\\sigma \(r_{\\theta }\(x,y_{w}\)-r_{\\theta }\(x,y_{l}\)\)\)\]=-{\\frac {1}{K \\choose 2}}E_{\(x,y_{w},y_{l}\)}\\log \\left\[{\\frac {e^{r_{\\theta }\(x,y_{w}\)}}{e^{r_{\\theta }\(x,y_{w}\)}+e^{r_{\\theta }\(x,y_{l}\)}}}\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/932c1c52b4564453776becf8604c8f9d9bbb90df)
where  K {\displaystyle K} ![{\\displaystyle K}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2b76fce82a62ed5461908f0dc8f037de4e3686b0) is the number of responses the labelers ranked,  r θ ( x , y ) {\displaystyle r_{\theta }(x,y)} ![{\\displaystyle r_{\\theta }\(x,y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0d7c2559912bddcae53009aaf05ea321f5ef9726) is the output of the reward model for prompt  x {\displaystyle x} ![{\\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) and completion  y {\displaystyle y} ![{\\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d),  y w {\displaystyle y_{w}} ![{\\displaystyle y_{w}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/67bb3f7963029d9c3e179e91f221e7d97cb8aad9) is the preferred completion over  y l {\displaystyle y_{l}} ![{\\displaystyle y_{l}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/26585cd35d275edc7e4ae324596c6887f735797c),  σ ( x ) {\displaystyle \sigma (x)} ![{\\displaystyle \\sigma \(x\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ae09ff47b50183fbfd1ea5697c63963ec9eefa20) denotes the [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function "Sigmoid function"), and  E [ X ] {\displaystyle E[X]} ![{\\displaystyle E\[X\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e455a34363c03fc5df8208d8b81fa29e3cdd524e) denotes the [expected value](https://en.wikipedia.org/wiki/Expected_value "Expected value").[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17) This can be thought of as a form of [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression "Logistic regression"), where the model predicts the probability that a response  y w {\displaystyle y_{w}} ![{\\displaystyle y_{w}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/67bb3f7963029d9c3e179e91f221e7d97cb8aad9) is preferred over  y l {\displaystyle y_{l}} ![{\\displaystyle y_{l}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/26585cd35d275edc7e4ae324596c6887f735797c). 
This loss function essentially measures the difference between the reward model's predictions and the decisions made by humans. The goal is to make the model's guesses as close as possible to the humans' preferences by minimizing the difference measured by this equation. In the case of only pairwise comparisons,  K = 2 {\displaystyle K=2} ![{\\displaystyle K=2}](https://wikimedia.org/api/rest_v1/media/math/render/svg/63b09257ec17c60892f31beed55b0f15608ebcb3), so the factor of  1 / ( K 2 ) = 1 {\displaystyle 1/{\tbinom {K}{2}}=1} ![{\\displaystyle 1/{\\tbinom {K}{2}}=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fcf04132fb623769086551e4f9604c3351916922).[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16) In general, all  ( K 2 ) {\displaystyle {\tbinom {K}{2}}} ![{\\displaystyle {\\tbinom {K}{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9aa8d6efecf96b1b6dfe3544832a74712febc950) comparisons from each prompt are used for training as a single [batch](https://en.wikipedia.org/wiki/Batch_learning "Batch learning").[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)
After training, the outputs of the model are normalized such that the reference completions have a mean score of 0. That is,[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16) ∑ y r θ ( x , y ) = 0 {\textstyle \sum _{y}r_{\theta }(x,y)=0} ![{\\textstyle \\sum _{y}r_{\\theta }\(x,y\)=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5fc9fe4ad9f0cabf1c41cc03b08fee040e31ede0) for each query and reference pair  ( x , y ) {\displaystyle (x,y)} ![{\\displaystyle \(x,y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/41cf50e4a314ca8e2c30964baa8d26e5be7a9386) by calculating the mean reward across the training dataset and setting it as the bias in the reward head. 
### Policy
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=6 "Edit section: Policy")]  
| [![icon](https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png)](https://en.wikipedia.org/wiki/File:Question_book-new.svg)  | This section **needs additional citations for[verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](https://en.wikipedia.org/wiki/Special:EditPage/Reinforcement_learning_from_human_feedback "Special:EditPage/Reinforcement learning from human feedback") by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners") in this section. Unsourced material may be challenged and removed. _( March 2026)__([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  |  
| --- | --- |  
The **policy model** is a function that takes a string as input, and produces another string. Usually in language modeling, the output string is not produced in one forward pass, but by multiple forward passes, generated autoregressively. Similarly to the reward model, the human feedback policy is also initialized from a pre-trained model.[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16)
The key is to understand language generation as if it is a game to be learned by RL. In RL, a policy is a function that maps a game state to a game action. In RLHF, the "game" is the game of replying to prompts. A prompt and all previously generated tokens are the game state, and generating a new token is a game action.[[41]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-41)
The first step in its training is supervised fine-tuning (SFT). This step does not require the reward model. Instead, the pre-trained model is trained on a dataset  D S F T {\displaystyle D_{SFT}} ![{\\displaystyle D_{SFT}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f119db3a455fd7c504249737d806d8e2dee72ece) that contains prompt-response pairs  ( x , y ) {\displaystyle (x,y)} ![{\\displaystyle \(x,y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/41cf50e4a314ca8e2c30964baa8d26e5be7a9386). Then, during SFT, the model is trained to auto-regressively generate the corresponding response  y {\displaystyle y} ![{\\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) when given a random prompt  x {\displaystyle x} ![{\\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4). The original paper recommends to SFT for only one epoch, since more than that causes overfitting. 
The dataset  D S F T {\displaystyle D_{SFT}} ![{\\displaystyle D_{SFT}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f119db3a455fd7c504249737d806d8e2dee72ece) is usually written by human contractors, who write both the prompts and responses. 
The second step uses a [policy gradient method](https://en.wikipedia.org/wiki/Policy_gradient_method "Policy gradient method") to the reward model. It uses a dataset  D R L {\displaystyle D_{RL}} ![{\\displaystyle D_{RL}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/253f1d9517f7b53455a2ac1f20acd8019c2cc8e4), which contains prompts, but not responses. Like most policy gradient methods, this algorithm has an outer loop and two inner loops: 
  * Initialize the policy  π ϕ R L {\displaystyle \pi _{\phi }^{RL}} ![{\\displaystyle \\pi _{\\phi }^{RL}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f62146621a5751333d470092159b92adc27e4785) to  π S F T {\displaystyle \pi ^{SFT}} ![{\\displaystyle \\pi ^{SFT}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/72e68cb7f821f0eab9fb424a0bd3bd5535c632e5), the policy output from SFT.
  * Loop for many steps. 
    * Initialize a new empty dataset  D π ϕ R L {\displaystyle D_{\pi _{\phi }^{RL}}} ![{\\displaystyle D_{\\pi _{\\phi }^{RL}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fa772d74a2a009fa3185603bf0dc35335c72da37).
    * Loop for many steps 
      * Sample a random prompt  x {\displaystyle x} ![{\\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) from  D R L {\displaystyle D_{RL}} ![{\\displaystyle D_{RL}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/253f1d9517f7b53455a2ac1f20acd8019c2cc8e4).
      * Generate a response  y {\displaystyle y} ![{\\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) from the policy  π ϕ R L {\displaystyle \pi _{\phi }^{RL}} ![{\\displaystyle \\pi _{\\phi }^{RL}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f62146621a5751333d470092159b92adc27e4785).
      * Calculate the reward signal  r θ ( x , y ) {\displaystyle r_{\theta }(x,y)} ![{\\displaystyle r_{\\theta }\(x,y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0d7c2559912bddcae53009aaf05ea321f5ef9726) from the reward model  r θ {\displaystyle r_{\theta }} ![{\\displaystyle r_{\\theta }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6ff5feaf63f6f1bbb6cd66f52cd2942d4da69def).
      * Add the triple  ( x , y , r θ ( x , y ) ) {\displaystyle (x,y,r_{\theta }(x,y))} ![{\\displaystyle \(x,y,r_{\\theta }\(x,y\)\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/159be45c20435a89d4eb718ac421959d948bc21d) to  D π ϕ R L {\displaystyle D_{\pi _{\phi }^{RL}}} ![{\\displaystyle D_{\\pi _{\\phi }^{RL}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fa772d74a2a009fa3185603bf0dc35335c72da37).
    * Update  ϕ {\displaystyle \phi } ![{\\displaystyle \\phi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/72b1f30316670aee6270a28334bdf4f5072cdde4) by a policy gradient method to increase the objective function objective ( ϕ ) = E ( x , y ) ∼ D π ϕ RL [ r θ ( x , y ) − β log ⁡ ( π ϕ RL ( y | x ) π SFT ( y | x ) ) ] {\displaystyle {\text{objective}}(\phi )=E_{(x,y)\sim D_{\pi _{\phi }^{\text{RL}}}}\left[r_{\theta }(x,y)-\beta \log \left({\frac {\pi _{\phi }^{\text{RL}}(y|x)}{\pi ^{\text{SFT}}(y|x)}}\right)\right]} ![{\\displaystyle {\\text{objective}}\(\\phi \)=E_{\(x,y\)\\sim D_{\\pi _{\\phi }^{\\text{RL}}}}\\left\[r_{\\theta }\(x,y\)-\\beta \\log \\left\({\\frac {\\pi _{\\phi }^{\\text{RL}}\(y|x\)}{\\pi ^{\\text{SFT}}\(y|x\)}}\\right\)\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/24db764b9a5965f060398f110042a364b8bdb67f)


Note that  ( x , y ) ∼ D π ϕ RL {\displaystyle (x,y)\sim D_{\pi _{\phi }^{\text{RL}}}} ![{\\displaystyle \(x,y\)\\sim D_{\\pi _{\\phi }^{\\text{RL}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d0231aa7ddfcf2bb1f7640713360bacba8546511) is equivalent to  x ∼ D R L , y ∼ π ϕ RL ( ⋅ | x ) {\displaystyle x\sim D_{RL},y\sim \pi _{\phi }^{\text{RL}}(\cdot |x)} ![{\\displaystyle x\\sim D_{RL},y\\sim \\pi _{\\phi }^{\\text{RL}}\(\\cdot |x\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a2e107589d57aca9b0910bf1414e774f3e444e68), which means "sample a prompt from  D R L {\displaystyle D_{RL}} ![{\\displaystyle D_{RL}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/253f1d9517f7b53455a2ac1f20acd8019c2cc8e4), then sample a response from the policy". 
The objective function has two parts. The first part is simply the expected reward  E [ r ] {\displaystyle E[r]} ![{\\displaystyle E\[r\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c4e721062d846a74c750775df431f6705c7bdd7e), and is standard for any RL algorithm. The second part is a "penalty term" involving the [KL divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence "Kullback–Leibler divergence"). The strength of the penalty term is determined by the hyperparameter  β {\displaystyle \beta } ![{\\displaystyle \\beta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ed48a5e36207156fb792fa79d29925d2f7901e8). 
This KL term works by penalizing the KL divergence (a measure of [statistical distance](https://en.wikipedia.org/wiki/Statistical_distance "Statistical distance") between distributions) between the model being fine-tuned and the initial supervised model. By choosing an appropriate  β {\displaystyle \beta } ![{\\displaystyle \\beta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ed48a5e36207156fb792fa79d29925d2f7901e8), the training can balance learning from new data while retaining useful information from the initial model, increasing [generalization](https://en.wikipedia.org/wiki/Generalization_\(learning\) "Generalization \(learning\)") by avoiding [fitting too closely](https://en.wikipedia.org/wiki/Overfitting "Overfitting") to the new data. Aside from preventing the new model from producing outputs too dissimilar those of the initial model, a second motivation of including the KL term is to encourage the model to output high-[entropy](https://en.wikipedia.org/wiki/Statistical_entropy "Statistical entropy") text, so as to prevent the model from [collapsing to a small number of canned responses](https://en.wikipedia.org/wiki/Mode_collapse "Mode collapse").[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16)
In simpler terms, the objective function calculates how well the policy's responses are expected to align with human feedback. The policy generates responses to prompts, and each response is evaluated both on how well it matches human preferences (as measured by the reward model) and how similar it is to responses the model would naturally generate. The goal is to balance improving alignment with human preferences while ensuring the model's responses remain diverse and not too far removed from what it has learned during its initial training. This helps the model not only to provide answers that people find useful or agreeable but also to maintain a broad understanding and avoid overly narrow or repetitive responses. 
### Proximal policy optimization
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=7 "Edit section: Proximal policy optimization")]
Main article: [Policy gradient method § Proximal Policy Optimization](https://en.wikipedia.org/wiki/Policy_gradient_method#Proximal_Policy_Optimization "Policy gradient method")
The policy function is usually trained by [proximal policy optimization](https://en.wikipedia.org/wiki/Policy_gradient_method#Proximal_Policy_Optimization_\(PPO\) "Policy gradient method") (PPO) algorithm. That is, the parameter  ϕ {\displaystyle \phi } ![{\\displaystyle \\phi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/72b1f30316670aee6270a28334bdf4f5072cdde4) is trained by gradient ascent on the clipped surrogate function.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16)
Classically, the PPO algorithm employs [generalized advantage estimation](https://en.wikipedia.org/wiki/Policy_gradient_method "Policy gradient method"), which means that there is an extra _value estimator_ V ξ t ( x ) {\displaystyle V_{\xi _{t}}(x)} ![{\\displaystyle V_{\\xi _{t}}\(x\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2aa46839469f194ac5cfc8433cf7d0a4c29f84d9), that updates concurrently with the policy  π ϕ t R L {\displaystyle \pi _{\phi _{t}}^{RL}} ![{\\displaystyle \\pi _{\\phi _{t}}^{RL}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f6c0fab17206f45d935cb0945564b721096ab733) during PPO training:  π ϕ t R L , V ξ t , π ϕ t + 1 R L , V ξ t + 1 , … {\displaystyle \pi _{\phi _{t}}^{RL},V_{\xi _{t}},\pi _{\phi _{t+1}}^{RL},V_{\xi _{t+1}},\dots } ![{\\displaystyle \\pi _{\\phi _{t}}^{RL},V_{\\xi _{t}},\\pi _{\\phi _{t+1}}^{RL},V_{\\xi _{t+1}},\\dots }](https://wikimedia.org/api/rest_v1/media/math/render/svg/037c337327255b19b85faf58f261d7422e43b39d).[[42]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-42) The value estimator is used only during training, and not outside of training. 
The PPO uses gradient descent on the following _clipped surrogate advantage_ : L PPO ( ϕ ) := E x ∼ D RL , y ∼ π ϕ t ( y | x ) [ min ( π ϕ R L ( y | x ) π ϕ t R L ( y | x ) A ( x , y ) , c l i p ( π ϕ R L ( y | x ) π ϕ t R L ( y | x ) , 1 − ϵ , 1 + ϵ ) A ( x , y ) ) ] {\displaystyle L_{\text{PPO}}(\phi ):=E_{x\sim D_{\text{RL}},y\sim \pi _{\phi _{t}}(y|x)}\left[\min \left({\frac {\pi _{\phi }^{RL}(y|x)}{\pi _{\phi _{t}}^{RL}(y|x)}}A(x,y),\mathrm {clip} \left({\frac {\pi _{\phi }^{RL}(y|x)}{\pi _{\phi _{t}}^{RL}(y|x)}},1-\epsilon ,1+\epsilon \right)A(x,y)\right)\right]} ![{\\displaystyle L_{\\text{PPO}}\(\\phi \):=E_{x\\sim D_{\\text{RL}},y\\sim \\pi _{\\phi _{t}}\(y|x\)}\\left\[\\min \\left\({\\frac {\\pi _{\\phi }^{RL}\(y|x\)}{\\pi _{\\phi _{t}}^{RL}\(y|x\)}}A\(x,y\),\\mathrm {clip} \\left\({\\frac {\\pi _{\\phi }^{RL}\(y|x\)}{\\pi _{\\phi _{t}}^{RL}\(y|x\)}},1-\\epsilon ,1+\\epsilon \\right\)A\(x,y\)\\right\)\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f6aa343cfce014022220e379ddd1d862209528d0)
where the advantage term  A ( x , y ) {\displaystyle A(x,y)} ![{\\displaystyle A\(x,y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/301b7810250db19125d15b511054cc06fd5f9a2f) is defined as  r θ ( x , y ) − V ξ t ( x ) {\displaystyle r_{\theta }(x,y)-V_{\xi _{t}}(x)} ![{\\displaystyle r_{\\theta }\(x,y\)-V_{\\xi _{t}}\(x\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5dc17c0195cc68c98614677742d04c6423db01b9). That is, the advantage is computed as the difference between the reward (the expected return) and the value estimation (the expected return from the policy). This is used to train the policy by gradient _ascent_ on it, usually using a standard momentum-gradient optimizer, like the [Adam optimizer](https://en.wikipedia.org/wiki/Adam_optimizer "Adam optimizer"). 
The original paper initialized the value estimator from the trained reward model.[[16]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-summarizationpaper-16) Since PPO is an actor-critic algorithm, the value estimator is updated concurrently with the policy, via minimizing the squared TD-error, which in this case equals the squared advantage term: L TD ( ξ ) = E ( x , y ) ∼ D π ϕ t RL [ ( r θ ( x , y ) − β log ⁡ ( π ϕ t RL ( y | x ) π SFT ( y | x ) ) − V ξ ( x ) ) 2 ] {\displaystyle L_{\text{TD}}(\xi )=\mathbb {E} _{(x,y)\sim D{\pi _{\phi _{t}}^{\text{RL}}}}\left[\left(r_{\theta }(x,y)-\beta \log \left({\frac {\pi _{\phi _{t}}^{\text{RL}}(y|x)}{\pi ^{\text{SFT}}(y|x)}}\right)-V_{\xi }(x)\right)^{2}\right]} ![{\\displaystyle L_{\\text{TD}}\(\\xi \)=\\mathbb {E} _{\(x,y\)\\sim D{\\pi _{\\phi _{t}}^{\\text{RL}}}}\\left\[\\left\(r_{\\theta }\(x,y\)-\\beta \\log \\left\({\\frac {\\pi _{\\phi _{t}}^{\\text{RL}}\(y|x\)}{\\pi ^{\\text{SFT}}\(y|x\)}}\\right\)-V_{\\xi }\(x\)\\right\)^{2}\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1b3de951e04f295815a74f1b30313da148e2976f)which is minimized by gradient _descent_ on it. Other methods than squared TD-error might be used. See the [actor-critic algorithm](https://en.wikipedia.org/wiki/Actor-critic_algorithm "Actor-critic algorithm") page for details. 
### Mixing pretraining gradients
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=8 "Edit section: Mixing pretraining gradients")]
A third term is commonly added to the objective function to prevent the model from catastrophic forgetting. For example, if the model is only trained in customer service, then it might forget general knowledge in geography. To prevent this, the RLHF process incorporates the original language modeling objective. That is, some random texts  x {\displaystyle x} ![{\\displaystyle x}](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) are sampled from the original pretraining dataset  D pretrain {\displaystyle D_{\text{pretrain}}} ![{\\displaystyle D_{\\text{pretrain}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/60772c56a176fbe7c73cd6716427660ed78235aa), and the model is trained to maximize the log-likelihood of the text  log ⁡ ( π ϕ R L ( x ) ) {\displaystyle \log(\pi _{\phi }^{RL}(x))} ![{\\displaystyle \\log\(\\pi _{\\phi }^{RL}\(x\)\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d07da0e1fe65ffe384fd409ae42293a9a5214c55). The final objective function is written as: 
L ( ϕ ) = E ( x , y ) ∼ D π ϕ RL [ r θ ( x , y ) − β log ⁡ ( π ϕ RL ( y | x ) π SFT ( y | x ) ) ] + γ E x ∼ D pretrain [ log ⁡ ( π ϕ RL ( x ) ) ] {\displaystyle L(\phi )=E_{(x,y)\sim D_{\pi _{\phi }^{\text{RL}}}}\left[r_{\theta }(x,y)-\beta \log \left({\frac {\pi _{\phi }^{\text{RL}}(y|x)}{\pi ^{\text{SFT}}(y|x)}}\right)\right]+\gamma E_{x\sim D_{\text{pretrain}}}[\log(\pi _{\phi }^{\text{RL}}(x))]} ![{\\displaystyle L\(\\phi \)=E_{\(x,y\)\\sim D_{\\pi _{\\phi }^{\\text{RL}}}}\\left\[r_{\\theta }\(x,y\)-\\beta \\log \\left\({\\frac {\\pi _{\\phi }^{\\text{RL}}\(y|x\)}{\\pi ^{\\text{SFT}}\(y|x\)}}\\right\)\\right\]+\\gamma E_{x\\sim D_{\\text{pretrain}}}\[\\log\(\\pi _{\\phi }^{\\text{RL}}\(x\)\)\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4238e2879bec95e2bf3b49ebbef9be802dee86d3)
where  γ {\displaystyle \gamma } ![{\\displaystyle \\gamma }](https://wikimedia.org/api/rest_v1/media/math/render/svg/a223c880b0ce3da8f64ee33c4f0010beee400b1a) controls the strength of this pretraining term.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17) This combined objective function is called PPO-ptx, where "ptx" means "Mixing Pretraining Gradients".[[9]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-:0-9) It was first used in the InstructGPT paper.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)
In total, this objective function defines the method for adjusting the RL policy, blending the aim of aligning with human feedback and maintaining the model's original language understanding. 
So, writing out fully explicitly, the PPO-ptx objective function is: 
L PPO-ptx ( ϕ ) := E ( x , y ) ∼ D π ϕ t RL [ min ( π ϕ R L ( y | x ) π ϕ t R L ( y | x ) A ( x , y ) , c l i p ( π ϕ R L ( y | x ) π ϕ t R L ( y | x ) , 1 − ϵ , 1 + ϵ ) A ( x , y ) ) − β log ⁡ ( π ϕ RL ( y | x ) π SFT ( y | x ) ) ] + γ E x ∼ D pretrain [ log ⁡ ( π ϕ RL ( x ) ) ] {\displaystyle {\begin{aligned}L_{\text{PPO-ptx}}(\phi )&:=E_{(x,y)\sim D_{\pi _{\phi _{t}}^{\text{RL}}}}\left[\min \left({\frac {\pi _{\phi }^{RL}(y|x)}{\pi _{\phi _{t}}^{RL}(y|x)}}A(x,y),\mathrm {clip} \left({\frac {\pi _{\phi }^{RL}(y|x)}{\pi _{\phi _{t}}^{RL}(y|x)}},1-\epsilon ,1+\epsilon \right)A(x,y)\right)-\beta \log \left({\frac {\pi _{\phi }^{\text{RL}}(y|x)}{\pi ^{\text{SFT}}(y|x)}}\right)\right]\\\&+\gamma E_{x\sim D_{\text{pretrain}}}[\log(\pi _{\phi }^{\text{RL}}(x))]\end{aligned}}} ![{\\displaystyle {\\begin{aligned}L_{\\text{PPO-ptx}}\(\\phi \)&:=E_{\(x,y\)\\sim D_{\\pi _{\\phi _{t}}^{\\text{RL}}}}\\left\[\\min \\left\({\\frac {\\pi _{\\phi }^{RL}\(y|x\)}{\\pi _{\\phi _{t}}^{RL}\(y|x\)}}A\(x,y\),\\mathrm {clip} \\left\({\\frac {\\pi _{\\phi }^{RL}\(y|x\)}{\\pi _{\\phi _{t}}^{RL}\(y|x\)}},1-\\epsilon ,1+\\epsilon \\right\)A\(x,y\)\\right\)-\\beta \\log \\left\({\\frac {\\pi _{\\phi }^{\\text{RL}}\(y|x\)}{\\pi ^{\\text{SFT}}\(y|x\)}}\\right\)\\right\]\\\\&+\\gamma E_{x\\sim D_{\\text{pretrain}}}\[\\log\(\\pi _{\\phi }^{\\text{RL}}\(x\)\)\]\\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cb7c3d30d05bcca11cb32799f3a2f29eaccf79d2) which is optimized by gradient _ascent_ on it. 
## Limitations
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=9 "Edit section: Limitations")]
RLHF suffers from challenges with collecting human feedback, learning a reward model, and optimizing the policy.[[43]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openproblems-43) Compared to data collection for techniques like [unsupervised](https://en.wikipedia.org/wiki/Unsupervised_learning "Unsupervised learning") or [self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning"), collecting data for RLHF is less scalable and more expensive. Its quality and consistency may vary depending on the task, interface, and the preferences and biases of individual humans.[[17]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-instructgptpaper-17)[[44]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-44)
The effectiveness of RLHF depends on the quality of human feedback. For instance, the model may become [biased](https://en.wikipedia.org/wiki/Algorithmic_bias "Algorithmic bias"), favoring certain groups over others, if the feedback lacks impartiality, is inconsistent, or is incorrect.[[5]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-huggingface-5)[[45]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-45) There is a risk of [overfitting](https://en.wikipedia.org/wiki/Overfit "Overfit"), where the model memorizes specific feedback examples instead of learning to [generalize](https://en.wikipedia.org/wiki/Generalization_\(learning\) "Generalization \(learning\)"). For instance, feedback predominantly from a specific demographic might lead the model to learn peculiarities or noise, along with the intended alignment. Excessive alignment to the specific feedback it received (that is, to the bias therein) can lead to the model performing sub-optimally in new contexts or when used by different groups.[[46]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-46) A single reward function cannot always represent the opinions of diverse groups of people. Even with a representative sample, conflicting views and preferences may result in the reward model favoring the majority's opinion, potentially disadvantaging underrepresented groups.[[43]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openproblems-43)
In some cases, as is possible in regular [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning"), there may be a risk of the model learning to manipulate the feedback process or [game the system](https://en.wikipedia.org/wiki/Game_the_system "Game the system") to achieve higher rewards rather than genuinely improving its performance.[[47]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-47) In the case of RLHF, a model may learn to exploit the fact that it is rewarded for what is evaluated positively and not necessarily for what is actually good, which can lead to it learning to persuade and manipulate. For example, models might learn that apparent confidence, even if inaccurate, garners higher rewards. Such behavior, if unchecked, is not just incentivized but can cause significant deployment issues due to the model's potential to mislead. Studies have found that humans are not skilled at identifying mistakes in LLM outputs in complex tasks; therefore, models learning to generate confident-sounding yet incorrect text can lead to significant issues when deployed.[[43]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-openproblems-43)
## Alternatives
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=10 "Edit section: Alternatives")]
### Reinforcement learning from AI feedback
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=11 "Edit section: Reinforcement learning from AI feedback")]
Similarly to RLHF, _reinforcement learning from AI feedback_ (RLAIF) relies on training a preference model, except that the feedback is automatically generated.[[48]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-48) This is notably used in [Anthropic](https://en.wikipedia.org/wiki/Anthropic "Anthropic")'s [constitutional AI](https://en.wikipedia.org/wiki/Constitutional_AI "Constitutional AI"), where the AI feedback is based on the conformance to the principles of a constitution.[[49]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-49)
### Direct alignment algorithms
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=12 "Edit section: Direct alignment algorithms")]
Direct alignment algorithms (DAA) have been proposed as a new class of algorithms[[50]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-50)[[51]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-51) that seek to directly optimize [large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") (LLMs) on human feedback data in a [supervised](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning") manner instead of the traditional policy-gradient methods. 
These algorithms aim to align models with human intent more transparently by removing the intermediate step of training a separate reward model. Instead of first predicting human preferences and then optimizing against those predictions, direct alignment methods train models end-to-end on human-labeled or curated outputs. This reduces potential misalignment risks introduced by proxy objectives or reward hacking. 
By directly optimizing for the behavior preferred by humans, these approaches often enable tighter alignment with human values, improved [interpretability](https://en.wikipedia.org/wiki/Interpretability_\(machine_learning\) "Interpretability \(machine learning\)"), and simpler training pipelines compared to RLHF. 
#### Direct preference optimization
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=13 "Edit section: Direct preference optimization")]
Direct preference optimization (DPO) is a technique to learn human preferences. Like RLHF, it has been applied to [align](https://en.wikipedia.org/wiki/AI_alignment "AI alignment") pre-trained large language models using human-generated preference data. Unlike RLHF, however, which first trains a separate intermediate model to understand what good outcomes look like and then teaches the main model how to achieve those outcomes, DPO simplifies the process by directly adjusting the main model according to people's preferences. It uses a [change of variables](https://en.wikipedia.org/wiki/Change_of_variables "Change of variables") to define the "preference [loss](https://en.wikipedia.org/wiki/Loss_function "Loss function")" directly as a function of the policy and uses this loss to [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\) "Fine-tuning \(deep learning\)") the model, helping it understand and prioritize human preferences without needing a separate step. Essentially, this approach directly shapes the model's decisions based on positive or negative human feedback. 
Recall, the pipeline of RLHF is as follows: 
  * We begin by gathering human preference dataset  D {\displaystyle D} ![{\\displaystyle D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f34a0c600395e5d4345287e21fb26efd386990e6).
  * We then fit a reward model  r ∗ {\displaystyle r^{*}} ![{\\displaystyle r^{*}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cc488e611bcc916d2da5dec54181e4909297e088) to data, by [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation "Maximum likelihood estimation") using the [Plackett–Luce model](https://en.wikipedia.org/wiki/Plackett%E2%80%93Luce_model "Plackett–Luce model") r ∗ = arg ⁡ max r E ( x , y 1 , … , y N ) ∼ D [ ln ⁡ ∏ k = 1 N e r ( x , y k ) ∑ i = k N e r ( x , y i ) ] {\displaystyle r^{*}=\arg \max _{r}\mathbb {E} _{(x,y_{1},\dots ,y_{N})\sim D}\left[\ln \prod _{k=1}^{N}{\frac {e^{r(x,y_{k})}}{\sum _{i=k}^{N}e^{r(x,y_{i})}}}\right]} ![{\\displaystyle r^{*}=\\arg \\max _{r}\\mathbb {E} _{\(x,y_{1},\\dots ,y_{N}\)\\sim D}\\left\[\\ln \\prod _{k=1}^{N}{\\frac {e^{r\(x,y_{k}\)}}{\\sum _{i=k}^{N}e^{r\(x,y_{i}\)}}}\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3cc934e23ce15264ba575deac7d2f5dc3e1d54c4)
  * We finally train an optimal policy  π ∗ {\displaystyle \pi ^{*}} ![{\\displaystyle \\pi ^{*}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f44ad69ec033a9a86437b2edaf620ea0b2c3f494) that maximizes the objective function: π ∗ = arg ⁡ max π RL E ( x , y ) ∼ D π RL [ r ∗ ( x , y ) − β log ⁡ ( π RL ( y | x ) π SFT ( y | x ) ) ] {\displaystyle \pi ^{*}=\arg \max _{\pi ^{\text{RL}}}\mathbb {E} _{(x,y)\sim D_{\pi ^{\text{RL}}}}\left[r^{*}(x,y)-\beta \log \left({\frac {\pi ^{\text{RL}}(y|x)}{\pi ^{\text{SFT}}(y|x)}}\right)\right]} ![{\\displaystyle \\pi ^{*}=\\arg \\max _{\\pi ^{\\text{RL}}}\\mathbb {E} _{\(x,y\)\\sim D_{\\pi ^{\\text{RL}}}}\\left\[r^{*}\(x,y\)-\\beta \\log \\left\({\\frac {\\pi ^{\\text{RL}}\(y|x\)}{\\pi ^{\\text{SFT}}\(y|x\)}}\\right\)\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/910bdb2195afccad84d2bb149a81269588b41fae)


However, instead of doing the intermediate step of the reward model, DPO directly optimizes for the final policy. 
First, solve directly for the optimal policy, which can be done by [Lagrange multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier "Lagrange multiplier"), as usual in [statistical mechanics](https://en.wikipedia.org/wiki/Statistical_mechanics "Statistical mechanics"): π ∗ ( y | x ) = π SFT ( y | x ) exp ⁡ ( r ∗ ( x , y ) / β ) Z ( x ) , {\displaystyle \pi ^{*}(y|x)={\frac {\pi ^{\text{SFT}}(y|x)\exp(r^{*}(x,y)/\beta )}{Z(x)}},} ![{\\displaystyle \\pi ^{*}\(y|x\)={\\frac {\\pi ^{\\text{SFT}}\(y|x\)\\exp\(r^{*}\(x,y\)/\\beta \)}{Z\(x\)}},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/846f500954c3662a2f8dceca7c74fe8d94bd6382)
where  Z ( x ) {\displaystyle Z(x)} ![{\\displaystyle Z\(x\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6c2ffb6f5d6e9eeab2867ef3c37ea13f9c294ac8) is the [partition function](https://en.wikipedia.org/wiki/Partition_function_\(statistical_mechanics\) "Partition function \(statistical mechanics\)"). This is unfortunately not tractable, since it requires summing over _all possible responses_ :  Z ( x ) = ∑ y π SFT ( y | x ) exp ⁡ ( r ∗ ( x , y ) / β ) = E y ∼ π SFT ( ⋅ | x ) [ exp ⁡ ( r ∗ ( x , y ) / β ) ] {\displaystyle Z(x)=\sum _{y}\pi ^{\text{SFT}}(y|x)\exp(r^{*}(x,y)/\beta )=\mathbb {E} _{y\sim \pi ^{\text{SFT}}(\cdot |x)}[\exp(r^{*}(x,y)/\beta )]} ![{\\displaystyle Z\(x\)=\\sum _{y}\\pi ^{\\text{SFT}}\(y|x\)\\exp\(r^{*}\(x,y\)/\\beta \)=\\mathbb {E} _{y\\sim \\pi ^{\\text{SFT}}\(\\cdot |x\)}\[\\exp\(r^{*}\(x,y\)/\\beta \)\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9390828a11020b55f7a25f01c4a63eefb23f5f98)
Next, invert this relationship to express the reward implicitly in terms of the optimal policy: r ∗ ( x , y ) = β log ⁡ π ∗ ( y | x ) π SFT ( y | x ) + β log ⁡ Z ( x ) . {\displaystyle r^{*}(x,y)=\beta \log {\frac {\pi ^{*}(y|x)}{\pi ^{\text{SFT}}(y|x)}}+\beta \log Z(x).} ![{\\displaystyle r^{*}\(x,y\)=\\beta \\log {\\frac {\\pi ^{*}\(y|x\)}{\\pi ^{\\text{SFT}}\(y|x\)}}+\\beta \\log Z\(x\).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2c2b8d924aa0460ee9d381f7a7009149df2837f7)
Finally, plug it back to the maximum likelihood estimator, we obtain[[52]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-:12-52): Appendix A  π ∗ = arg ⁡ max π E ( x , y 1 , … , y N ) ∼ D [ ln ⁡ ∏ k = 1 N e β log ⁡ π ( y k | x ) π SFT ( y k | x ) ∑ i = k N e β log ⁡ π ( y i | x ) π SFT ( y i | x ) ] {\displaystyle \pi ^{*}=\arg \max _{\pi }\mathbb {E} _{(x,y_{1},\dots ,y_{N})\sim D}\left[\ln \prod _{k=1}^{N}{\frac {e^{\beta \log {\frac {\pi (y_{k}|x)}{\pi ^{\text{SFT}}(y_{k}|x)}}}}{\sum _{i=k}^{N}e^{\beta \log {\frac {\pi (y_{i}|x)}{\pi ^{\text{SFT}}(y_{i}|x)}}}}}\right]} ![{\\displaystyle \\pi ^{*}=\\arg \\max _{\\pi }\\mathbb {E} _{\(x,y_{1},\\dots ,y_{N}\)\\sim D}\\left\[\\ln \\prod _{k=1}^{N}{\\frac {e^{\\beta \\log {\\frac {\\pi \(y_{k}|x\)}{\\pi ^{\\text{SFT}}\(y_{k}|x\)}}}}{\\sum _{i=k}^{N}e^{\\beta \\log {\\frac {\\pi \(y_{i}|x\)}{\\pi ^{\\text{SFT}}\(y_{i}|x\)}}}}}\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2e15148de094249e0b03bd20ee7d210e456a5941)
Usually, DPO is used for modeling human preference in pairwise comparisons, so that  N = 2 {\displaystyle N=2} ![{\\displaystyle N=2}](https://wikimedia.org/api/rest_v1/media/math/render/svg/405d64b14536deffc3465f1e81b1b7fe9358ad2a). In that case, we have π ∗ = arg ⁡ max π E ( x , y w , y l ) ∼ D [ log ⁡ σ ( β log ⁡ π ( y w | x ) π SFT ( y w | x ) − β log ⁡ π ( y l | x ) π SFT ( y l | x ) ) ] {\displaystyle \pi ^{*}=\arg \max _{\pi }\mathbb {E} _{(x,y_{w},y_{l})\sim D}\left[\log \sigma \left(\beta \log {\frac {\pi (y_{w}|x)}{\pi ^{\text{SFT}}(y_{w}|x)}}-\beta \log {\frac {\pi (y_{l}|x)}{\pi ^{\text{SFT}}(y_{l}|x)}}\right)\right]} ![{\\displaystyle \\pi ^{*}=\\arg \\max _{\\pi }\\mathbb {E} _{\(x,y_{w},y_{l}\)\\sim D}\\left\[\\log \\sigma \\left\(\\beta \\log {\\frac {\\pi \(y_{w}|x\)}{\\pi ^{\\text{SFT}}\(y_{w}|x\)}}-\\beta \\log {\\frac {\\pi \(y_{l}|x\)}{\\pi ^{\\text{SFT}}\(y_{l}|x\)}}\\right\)\\right\]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/65ea9926bcbc4d7fcd33c5e8a66f71ccd095a27f)
DPO eliminates the need for a separate reward model or reinforcement learning loop, treating alignment as a supervised learning problem over preference data. This is simpler to implement and train than RLHF and has been shown to produce comparable and sometimes superior results.[[52]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-:12-52) Nevertheless, RLHF has also been shown to beat DPO on some datasets, for example, on benchmarks that attempt to measure truthfulness. Therefore, the choice of method may vary depending on the features of the human preference data and the nature of the task.[[53]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-53)
#### Identity preference optimization
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=14 "Edit section: Identity preference optimization")]
Identity preference optimization (IPO)[[54]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-:22-54) is a modification to the original DPO objective that introduces a regularization term to reduce the chance of overfitting even when preference data is noisy. 
To solve this objective, IPO minimizes the quadratic loss function E x , y w , y l ∼ D [ h π ( x , y w , y l ) − 1 2 β − 1 ] 2 {\displaystyle {\begin{aligned}&\mathbb {E} _{x,y_{w},y_{l}\sim D}[h_{\pi }(x,y_{w},y_{l})-{\frac {1}{2}}\beta ^{-1}]^{2}\end{aligned}}} ![{\\displaystyle {\\begin{aligned}&\\mathbb {E} _{x,y_{w},y_{l}\\sim D}\[h_{\\pi }\(x,y_{w},y_{l}\)-{\\frac {1}{2}}\\beta ^{-1}\]^{2}\\end{aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e0bcf055b34ce7f57db73afcefb6699e2dbc4148) where  h π ( x , y w , y l ) = log ⁡ ( π θ ( y w | x ) π ref ( y w | x ) ) ) − log ⁡ ( π θ ( y l | x ) π ref ( y l | x ) ) {\displaystyle h_{\pi }(x,y_{w},y_{l})=\log \left({\frac {\pi _{\theta }(y_{w}|x)}{\pi _{\text{ref}}(y_{w}|x))}}\right)-\log \left({\frac {\pi _{\theta }(y_{l}|x)}{\pi _{\text{ref}}(y_{l}|x)}}\right)} ![{\\displaystyle h_{\\pi }\(x,y_{w},y_{l}\)=\\log \\left\({\\frac {\\pi _{\\theta }\(y_{w}|x\)}{\\pi _{\\text{ref}}\(y_{w}|x\)\)}}\\right\)-\\log \\left\({\\frac {\\pi _{\\theta }\(y_{l}|x\)}{\\pi _{\\text{ref}}\(y_{l}|x\)}}\\right\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8e6a6b27e863fe9061607bd73dff506a83d68cae). 
IPO can control the gap between the log-likelihood ratios of the policy model and the reference by always regularizing the solution towards the reference model. It allows learning directly from preferences without a reward modelling stage and without relying on the [Bradley-Terry modelling](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "Bradley–Terry model") assumption that assumes that pairwise preferences can be substituted with pointwise rewards.[[54]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-:22-54)
#### Kahneman-Tversky optimization
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=15 "Edit section: Kahneman-Tversky optimization")]
Kahneman-Tversky optimization (KTO)[[55]](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_note-55) is another direct alignment algorithm drawing from [prospect theory](https://en.wikipedia.org/wiki/Prospect_theory "Prospect theory") to model uncertainty in human decisions. Unlike DPO, KTO requires only a binary feedback signal (desirable or undesirable) instead of explicit preference pairs. 
The value function  v ( x , y ) {\displaystyle v(x,y)} ![{\\displaystyle v\(x,y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ca1cc47d643640c35af2867bd47f907af79574d4) is defined piecewise depending on whether  y {\displaystyle y} ![{\\displaystyle y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) is desirable ( λ D {\displaystyle \lambda _{D}} ![{\\displaystyle \\lambda _{D}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f2e5040a1dc6a5145caa1ed08a9bd0fd5587b684)) or undesirable ( λ U {\displaystyle \lambda _{U}} ![{\\displaystyle \\lambda _{U}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/65b587952de191a76ba03d8d303e94ceaaa1298b)): 
v ( x , y ) = { λ D σ ( β ( r θ ( x , y ) − z 0 ) ) , if  y ∼ y d e s i r a b l e ∣ x , λ U σ ( β ( z 0 − r θ ( x , y ) ) ) , if  y ∼ y u n d e s i r a b l e ∣ x {\displaystyle v(x,y)\;=\;{\begin{cases}\lambda _{D}\,\sigma \\!{\bigl (}\,\beta \,{\bigl (}r_{\theta }(x,y)\;-\;z_{0}{\bigr )}{\bigr )},&\quad {\text{if }}y\sim y_{\mathrm {desirable} \mid x},\\\\[6pt]\lambda _{U}\,\sigma \\!{\bigl (}\,\beta \,{\bigl (}z_{0}\;-\;r_{\theta }(x,y){\bigr )}{\bigr )},&\quad {\text{if }}y\sim y_{\mathrm {undesirable} \mid x}\end{cases}}} ![{\\displaystyle v\(x,y\)\\;=\\;{\\begin{cases}\\lambda _{D}\\,\\sigma \\!{\\bigl \(}\\,\\beta \\,{\\bigl \(}r_{\\theta }\(x,y\)\\;-\\;z_{0}{\\bigr \)}{\\bigr \)},&\\quad {\\text{if }}y\\sim y_{\\mathrm {desirable} \\mid x},\\\\\[6pt\]\\lambda _{U}\\,\\sigma \\!{\\bigl \(}\\,\\beta \\,{\\bigl \(}z_{0}\\;-\\;r_{\\theta }\(x,y\){\\bigr \)}{\\bigr \)},&\\quad {\\text{if }}y\\sim y_{\\mathrm {undesirable} \\mid x}\\end{cases}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8dc7aac144fb2d600c8453d160b0284b0d5e9df8)
Here,  β {\displaystyle \beta } ![{\\displaystyle \\beta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ed48a5e36207156fb792fa79d29925d2f7901e8) controls how “risk-averse” the value function is (larger  β {\displaystyle \beta } ![{\\displaystyle \\beta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ed48a5e36207156fb792fa79d29925d2f7901e8) = faster saturation in the logistic function  σ {\displaystyle \sigma } ![{\\displaystyle \\sigma }](https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36))and  z 0 = K L ( π θ ( y ′ ∣ x ) ‖ π r e f ( y ′ ∣ x ) ) {\textstyle z_{0}=\mathrm {KL} \\!{\Bigl (}\,\pi _{\theta }(y'\mid x)\;{\big \Vert }\;\pi _{\mathrm {ref} }(y'\mid x){\Bigr )}} ![{\\textstyle z_{0}=\\mathrm {KL} \\!{\\Bigl \(}\\,\\pi _{\\theta }\(y'\\mid x\)\\;{\\big \\Vert }\\;\\pi _{\\mathrm {ref} }\(y'\\mid x\){\\Bigr \)}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7b0098a3e5f2362cf5295008b76b109da43871d5)is a baseline given by the Kullback–Leibler divergence. Since many real-world feedback pipelines yield "like/dislike" data more easily than pairwise comparisons, KTO is designed to be data-efficient and to reflect "loss aversion" more directly by using a straightforward notion of "good vs. bad" at the example level. 
## See also
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=16 "Edit section: See also")]
  * [Human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop "Human-in-the-loop")
  * [Reward-based selection](https://en.wikipedia.org/wiki/Reward-based_selection "Reward-based selection")


## References
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=17 "Edit section: References")]
  1. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-1)** Kongot, Aparna (2025). [_Human-Centered AI: An Illustrated Scientific Quest (Human–Computer Interaction Series)_](https://www.google.com/books/edition/Human_Centered_AI_An_Illustrated_Scienti/XmNSEQAAQBAJ?hl=en&gbpv=1&dq=%22reinforcement+learning+from+human+feedback%22&pg=PA389&printsec=frontcover). Springer. p. 389. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-3031613746](https://en.wikipedia.org/wiki/Special:BookSources/978-3031613746 "Special:BookSources/978-3031613746").
  2. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-2)** Lan, Xuguang (2025). [_Intelligent Robotics and Applications: 17th International Conference, ICIRA 2024, Xi'an, China, July 31 – August 2, 2024, Proceedings, Part VIII (Lecture Notes in Computer Science Book 15208)_](https://www.google.com/books/edition/Intelligent_Robotics_and_Applications/icVAEQAAQBAJ?hl=en&gbpv=1&dq=%22reinforcement+learning+from+human+feedback%22&pg=PA6&printsec=frontcover). Springer. p. 6.
  3. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-3)** Russell, Stuart J.; Norvig, Peter (2016). _Artificial intelligence: a modern approach_ (Third, Global ed.). Boston Columbus Indianapolis New York San Francisco Upper Saddle River Amsterdam Cape Town Dubai London Madrid Milan Munich Paris Montreal Toronto Delhi Mexico City Sao Paulo Sydney Hong Kong Seoul Singapore Taipei Tokyo: Pearson. pp. 830–831. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-13-604259-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-604259-4 "Special:BookSources/978-0-13-604259-4").
  4. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-ziegler_4-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-ziegler_4-1) Ziegler, Daniel M.; Stiennon, Nisan; Wu, Jeffrey; Brown, Tom B.; Radford, Alec; Amodei, Dario; Christiano, Paul; Irving, Geoffrey (2019). "Fine-Tuning Language Models from Human Preferences". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1909.08593](https://arxiv.org/abs/1909.08593) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  5. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-huggingface_5-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-huggingface_5-1) [_**c**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-huggingface_5-2) [_**d**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-huggingface_5-3) Lambert, Nathan; Castricato, Louis; von Werra, Leandro; Havrilla, Alex. ["Illustrating Reinforcement Learning from Human Feedback (RLHF)"](https://huggingface.co/blog/rlhf). _huggingface.co_. Retrieved 4 March 2023.
  6. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-6)** Schulman, John; Wolski, Filip; Dhariwal, Prafulla; Radford, Alec; Klimov, Oleg (2017). "Proximal Policy Optimization Algorithms". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1707.06347](https://arxiv.org/abs/1707.06347) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  7. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-7)** Tuan, Yi-Lin; Zhang, Jinzhi; Li, Yujia; Lee, Hung-yi (2018). "Proximal Policy Optimization and its Dynamic Version for Sequence Generation". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1808.07982](https://arxiv.org/abs/1808.07982) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  8. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openai_8-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openai_8-1) [_**c**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openai_8-2) [_**d**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openai_8-3) [_**e**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openai_8-4) Amodei, Dario; Christiano, Paul; Ray, Alex (13 June 2017). ["Learning from human preferences"](https://openai.com/research/learning-from-human-preferences). _openai.com_. Retrieved 4 March 2023.
  9. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-:0_9-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-:0_9-1) Zheng, Rui; Dou, Shihan; Gao, Songyang; Hua, Yuan; Shen, Wei; Wang, Binghai; Liu, Yan; Jin, Senjie; Liu, Qin; Zhou, Yuhao; Xiong, Limao; Chen, Lu; Xi, Zhiheng; Xu, Nuo; Lai, Wenbin; Zhu, Minghao; Chang, Cheng; Yin, Zhangyue; Weng, Rongxiang; Cheng, Wensen; Huang, Haoran; Sun, Tianxiang; Yan, Hang; Gui, Tao; Zhang, Qi; Qiu, Xipeng; Huang, Xuanjing (2023). "Secrets of RLHF in Large Language Models Part I: PPO". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2307.04964](https://arxiv.org/abs/2307.04964) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  10. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-10)** Knox, W. Bradley; Stone, Peter; Breazeal, Cynthia (2013). ["Training a Robot via Human Feedback: A Case Study"](https://link.springer.com/chapter/10.1007/978-3-319-02675-6_46). _Social Robotics_. Lecture Notes in Computer Science. Vol. 8239. Springer International Publishing. pp. 460–470. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/978-3-319-02675-6_46](https://doi.org/10.1007%2F978-3-319-02675-6_46). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-3-319-02674-9](https://en.wikipedia.org/wiki/Special:BookSources/978-3-319-02674-9 "Special:BookSources/978-3-319-02674-9"). Retrieved 26 February 2024.
  11. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-11)** Akrour, Riad; Schoenauer, Marc; Sebag, Michèle (2012). ["APRIL: Active Preference Learning-Based Reinforcement Learning"](https://link.springer.com/chapter/10.1007/978-3-642-33486-3_8). _Machine Learning and Knowledge Discovery in Databases_. Lecture Notes in Computer Science. Vol. 7524. Springer. pp. 116–131. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1208.0984](https://arxiv.org/abs/1208.0984). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/978-3-642-33486-3_8](https://doi.org/10.1007%2F978-3-642-33486-3_8). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-3-642-33485-6](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-33485-6 "Special:BookSources/978-3-642-33485-6"). Retrieved 26 February 2024.
  12. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-12)** Wilson, Aaron; Fern, Alan; Tadepalli, Prasad (2012). ["A Bayesian Approach for Policy Learning from Trajectory Preference Queries"](https://papers.nips.cc/paper_files/paper/2012/hash/16c222aa19898e5058938167c8ab6c57-Abstract.html). _Advances in Neural Information Processing Systems_. **25**. Curran Associates, Inc. Retrieved 26 February 2024.
  13. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-13)** Schoenauer, Marc; Akrour, Riad; Sebag, Michele; Souplet, Jean-Christophe (18 June 2014). ["Programming by Feedback"](https://proceedings.mlr.press/v32/schoenauer14.html). _Proceedings of the 31st International Conference on Machine Learning_. PMLR: 1503–1511. Retrieved 26 February 2024.
  14. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-14)** Warnell, Garrett; Waytowich, Nicholas; Lawhern, Vernon; Stone, Peter (25 April 2018). "Deep TAMER: Interactive Agent Shaping in High-Dimensional State Spaces". _Proceedings of the AAAI Conference on Artificial Intelligence_. **32** (1). [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1709.10163](https://arxiv.org/abs/1709.10163). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1609/aaai.v32i1.11485](https://doi.org/10.1609%2Faaai.v32i1.11485). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [4130751](https://api.semanticscholar.org/CorpusID:4130751).
  15. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-15)** MacGlashan, James; Ho, Mark K.; Loftin, Robert; Peng, Bei; Wang, Guan; Roberts, David L.; Taylor, Matthew E.; Littman, Michael L. (6 August 2017). ["Interactive learning from policy-dependent human feedback"](https://dl.acm.org/doi/10.5555/3305890.3305917). _Proceedings of the 34th International Conference on Machine Learning - Volume 70_. JMLR.org: 2285–2294. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1701.06049](https://arxiv.org/abs/1701.06049).
  16. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-1) [_**c**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-2) [_**d**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-3) [_**e**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-4) [_**f**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-5) [_**g**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-6) [_**h**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-7) [_**i**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-8) [_**j**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-summarizationpaper_16-9) Nisan Stiennon; Long Ouyang; Jeffrey Wu; Daniel Ziegler; Ryan Lowe; Chelsea Voss; Alec Radford; Dario Amodei; Paul F. Christiano (2020). ["Learning to summarize with human feedback"](https://proceedings.neurips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html). _Advances in Neural Information Processing Systems_. **33**.
  17. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-1) [_**c**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-2) [_**d**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-3) [_**e**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-4) [_**f**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-5) [_**g**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-6) [_**h**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-7) [_**i**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-8) [_**j**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-9) [_**k**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-10) [_**l**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-instructgptpaper_17-11) Ouyang, Long; Wu, Jeffrey; Jiang, Xu; Almeida, Diogo; Wainwright, Carroll; Mishkin, Pamela; Zhang, Chong; Agarwal, Sandhini; Slama, Katarina; Gray, Alex; Schulman, John; Hilton, Jacob; Kelton, Fraser; Miller, Luke; Simens, Maddie; Askell, Amanda; Welinder, Peter; Christiano, Paul; Leike, Jan; Lowe, Ryan (31 October 2022). [_Training language models to follow instructions with human feedback_](https://openreview.net/forum?id=TG8KACxEON). Thirty-Sixth Conference on Neural Information Processing Systems: NeurIPS 2022. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2203.02155](https://arxiv.org/abs/2203.02155).
  18. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-18)** Bai, Yuntao; Jones, Andy; Ndousse, Kamal; Askell, Amanda; Chen, Anna; DasSarma, Nova; Drain, Dawn; Fort, Stanislav; Ganguli, Deep; Henighan, Tom; Joseph, Nicholas; Kadavath, Saurav; Kernion, Jackson; Conerly, Tom; El-Showk, Sheer; Elhage, Nelson; Hatfield-Dodds, Zac; Hernandez, Danny; Hume, Tristan; Johnston, Scott; Kravec, Shauna; Lovitt, Liane; Nanda, Neel; Olsson, Catherine; Amodei, Dario; Brown, Tom; Clark, Jack; McCandlish, Sam; Olah, Chris; Mann, Ben; Kaplan, Jared (2022). "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2204.05862](https://arxiv.org/abs/2204.05862) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  19. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-ars_19-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-ars_19-1) Edwards, Benj (1 December 2022). ["OpenAI invites everyone to test ChatGPT, a new AI-powered chatbot—with amusing results"](https://arstechnica.com/information-technology/2022/12/openai-invites-everyone-to-test-new-ai-powered-chatbot-with-amusing-results/). _Ars Technica_. Retrieved 4 March 2023.
  20. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-20)** Abhishek, Gupta (5 February 2023). ["Getting stakeholder engagement right in responsible AI"](https://venturebeat.com/ai/getting-stakeholder-engagement-right-in-responsible-ai/). _VentureBeat_. Retrieved 4 March 2023.
  21. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-21)** Fernandes, Patrick; Madaan, Aman; Liu, Emmy; Farinhas, António; Pedro Henrique Martins; Bertsch, Amanda; de Souza, José G. C.; Zhou, Shuyan; Wu, Tongshuang; Neubig, Graham; Martins, André F. T. (2023). "Bridging the Gap: A Survey on Integrating (Human) Feedback for Natural Language Generation". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2305.00955](https://arxiv.org/abs/2305.00955) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  22. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-xiejiang_22-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-xiejiang_22-1) Xie, Tengyang; Jiang, Nan; Wang, Huan; Xiong, Caiming; Bai, Yu (2021). ["Policy Finetuning: Bridging Sample-Efficient Offline and Online Reinforcement Learning"](https://proceedings.neurips.cc/paper/2021/hash/e61eaa38aed621dd776d0e67cfeee366-Abstract.html). _Advances in Neural Information Processing Systems_. **34**. Curran Associates, Inc.: 27395–27407. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2106.04895](https://arxiv.org/abs/2106.04895). Retrieved 10 March 2024.
  23. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-pacchiano_23-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-pacchiano_23-1) Pacchiano, Aldo; Saha, Aadirupa; Lee, Jonathan (2023-03-03). ["Dueling RL: Reinforcement Learning with Trajectory Preferences"](https://proceedings.mlr.press/v206/saha23a.html). _Proceedings of the 26th International Conference on Artificial Intelligence and Statistics_. PMLR: 6263–6289. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2111.04850](https://arxiv.org/abs/2111.04850).
  24. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-zhujordan_24-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-zhujordan_24-1) Zhu, Banghua; Jordan, Michael; Jiao, Jiantao (2023-07-03). ["Principled Reinforcement Learning with Human Feedback from Pairwise or K-wise Comparisons"](https://proceedings.mlr.press/v202/zhu23f.html). _Proceedings of the 40th International Conference on Machine Learning_. PMLR: 43037–43067. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2301.11270](https://arxiv.org/abs/2301.11270).
  25. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-25)** Li, Zihao; Yang, Zhuoran; Wang, Mengdi (20 June 2023). ["Reinforcement learning with Human Feedback: Learning Dynamic Choices via Pessimism"](https://openreview.net/forum?id=gxM2AUFMsK&referrer=%5Bthe%20profile%20of%20Zhuoran%20Yang%5D\(%2Fprofile%3Fid%3D~Zhuoran_Yang1\)). _ILHF Workshop ICML 2023_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2305.18438](https://arxiv.org/abs/2305.18438). Retrieved 10 March 2024.
  26. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-26)** Ouyang, Long; Wu, Jeff; Jiang, Xu; Almeida, Diogo; Wainwright, Carroll L.; Mishkin, Pamela; Zhang, Chong; Agarwal, Sandhini; Slama, Katarina; Ray, Alex; Schulman, John; Hilton, Jacob; Kelton, Fraser; Miller, Luke; Simens, Maddie; Askell, Amanda; Welinder, Peter; Christiano, Paul; Leike, Jan; Lowe, Ryan (2022). "Training language models to follow instructions with human feedback". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2203.02155](https://arxiv.org/abs/2203.02155) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  27. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-27)** Wiggers, Kyle (24 February 2023). ["Can AI really be protected from text-based attacks?"](https://techcrunch.com/2023/02/24/can-language-models-really-be-protected-from-text-based-attacks/). _TechCrunch_. Retrieved 4 March 2023.
  28. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-28)** Heikkilä, Melissa (21 February 2023). ["How OpenAI is trying to make ChatGPT safer and less biased"](https://www.technologyreview.com/2023/02/21/1068893/how-openai-is-trying-to-make-chatgpt-safer-and-less-biased/). _MIT Technology Review_. Retrieved 4 March 2023.
  29. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-29)** Douglas Heaven, Will (30 November 2022). ["ChatGPT is OpenAI's latest fix for GPT-3. It's slick but still spews nonsense"](https://www.technologyreview.com/2022/11/30/1063878/openai-still-fixing-gpt3-ai-large-language-model/). _MIT Technology Review_. Retrieved 4 March 2023.
  30. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-30)** Glaese, Amelia; McAleese, Nat; Trębacz, Maja; Aslanides, John; Firoiu, Vlad; Ewalds, Timo; Rauh, Maribeth; Weidinger, Laura; Chadwick, Martin; Thacker, Phoebe; Campbell-Gillingham, Lucy; Uesato, Jonathan; Huang, Po-Sen; Comanescu, Ramona; Yang, Fan; See, Abigail; Dathathri, Sumanth; Greig, Rory; Chen, Charlie; Fritz, Doug; Elias, Jaume Sanchez; Green, Richard; Mokrá, Soňa; Fernando, Nicholas; Wu, Boxi; Foley, Rachel; Young, Susannah; Gabriel, Iason; Isaac, William; Mellor, John; Hassabis, Demis; Kavukcuoglu, Koray; Hendricks, Lisa Anne; Irving, Geoffrey (2022). "Improving alignment of dialogue agents via targeted human judgements". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2209.14375](https://arxiv.org/abs/2209.14375) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  31. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-31)** Goldman, Sharon (23 September 2022). ["Why DeepMind isn't deploying its new AI chatbot — and what it means for responsible AI"](https://venturebeat.com/ai/why-deepmind-isnt-deploying-its-new-ai-chatbot). _VentureBeat_. Retrieved 4 March 2023.
  32. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-32)** The Sparrow team (22 September 2022). ["Building safer dialogue agents"](https://www.deepmind.com/blog/building-safer-dialogue-agents). _www.deepmind.com_. Retrieved 4 March 2023.
  33. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-33)** Pinchai, Sundar; Hassabis, Demis (6 December 2023). ["Introducing Gemini: our largest and most capable AI model"](https://blog.google/technology/ai/google-gemini-ai/). _Google_. Retrieved 29 February 2024.
  34. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-34)** Henshall, Will (18 July 2023). ["What to Know About Claude 2, Anthropic's Rival to ChatGPT"](https://time.com/6295523/claude-2-anthropic-chatgpt/). _TIME_. Retrieved 6 March 2024.
  35. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-35)** Fan, Ying; Watkins, Olivia; Du, Yuqing; Liu, Hao; Ryu, Moonkyung; Boutilier, Craig; Abbeel, Pieter; Ghavamzadeh, Mohammad; Lee, Kangwook; Lee, Kimin (2 November 2023). ["DPOK: Reinforcement Learning for Fine-tuning Text-to-Image Diffusion Models"](https://openreview.net/forum?id=8OTPepXzeh&referrer=%5Bthe%20profile%20of%20Moonkyung%20Ryu%5D\(%2Fprofile%3Fid%3D~Moonkyung_Ryu1\)). _NeurIPS 2023_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2305.16381](https://arxiv.org/abs/2305.16381). Retrieved 1 March 2024.
  36. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-36)** Xu, Jiazheng; Liu, Xiao; Wu, Yuchen; Tong, Yuxuan; Li, Qinkai; Ding, Ming; Tang, Jie; Dong, Yuxiao (15 December 2023). ["ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation"](https://proceedings.neurips.cc/paper_files/paper/2023/hash/33646ef0ed554145eab65f6250fab0c9-Abstract-Conference.html). _Advances in Neural Information Processing Systems_. **36** : 15903–15935. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2304.05977](https://arxiv.org/abs/2304.05977). Retrieved 1 March 2024.
  37. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-37)** Lee, Kimin; Liu, Hao; Ryu, Moonkyung; Watkins, Olivia; Du, Yuqing; Boutilier, Craig; Abbeel, Pieter; Ghavamzadeh, Mohammad; Gu, Shixiang Shane (2023). "Aligning Text-to-Image Models using Human Feedback". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2302.12192](https://arxiv.org/abs/2302.12192) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  38. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-38)** Leike, Jan; Martic, Miljan; Legg, Shane (12 June 2017). ["Learning through human feedback"](https://www.deepmind.com/blog/learning-through-human-feedback). _www.deepmind.com_. Retrieved 4 March 2023.
  39. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-39)** Christiano, Paul F; Leike, Jan; Brown, Tom; Martic, Miljan; Legg, Shane; Amodei, Dario (2017). ["Deep Reinforcement Learning from Human Preferences"](https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html). _Advances in Neural Information Processing Systems_. **30**. Curran Associates, Inc. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1706.03741](https://arxiv.org/abs/1706.03741). Retrieved 4 March 2023.
  40. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-40)** von Csefalvay, Chris (2026). "4. Reinforcement Learning: Better Each Time". _Post-Training: A Practical Guide for AI Engineers and Developers_. No Starch Press. pp. 114–116. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-7185-0520-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-7185-0520-9 "Special:BookSources/978-1-7185-0520-9").
  41. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-41)** Iusztin, Paul (2024). [_LLM Engineer's Handbook: Master the art of engineering large language models from concept to production_](https://www.google.com/books/edition/LLM_Engineer_s_Handbook/jHEqEQAAQBAJ?hl=en&gbpv=1&dq=%22reinforcement+learning+from+human+feedback%22&pg=PA246&printsec=frontcover). Packt Publishing. p. 246. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1836200079](https://en.wikipedia.org/wiki/Special:BookSources/978-1836200079 "Special:BookSources/978-1836200079").
  42. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-42)** von Csefalvay, Chris (2026). "5. Preference Optimization: Modern Alternatives to PPO". _Post-Training: A Practical Guide for AI Engineers and Developers_. No Starch Press. pp. 133–140. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-7185-0520-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-7185-0520-9 "Special:BookSources/978-1-7185-0520-9").
  43. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openproblems_43-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openproblems_43-1) [_**c**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-openproblems_43-2) Casper, Stephen; Davies, Xander; Shi, Claudia; Gilbert, Thomas Krendl; Scheurer, Jérémy; Rando, Javier; Freedman, Rachel; Korbak, Tomasz; Lindner, David; Freire, Pedro; Wang, Tony Tong; Marks, Samuel; Segerie, Charbel-Raphael; Carroll, Micah; Peng, Andi; Christoffersen, Phillip; Damani, Mehul; Slocum, Stewart; Anwar, Usman; Siththaranjan, Anand; Nadeau, Max; Michaud, Eric J.; Pfau, Jacob; Krasheninnikov, Dmitrii; Chen, Xin; Langosco, Lauro; Hase, Peter; Biyik, Erdem; Dragan, Anca; Krueger, David; Sadigh, Dorsa; Hadfield-Menell, Dylan (18 September 2023). ["Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback"](https://openreview.net/forum?id=bx24KpJ4Eb). _Transactions on Machine Learning Research_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2307.15217](https://arxiv.org/abs/2307.15217).
  44. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-44)** Christiano, Paul (25 January 2023). ["Thoughts on the impact of RLHF research"](https://www.alignmentforum.org/posts/vwu4kegAEZTBtpT6p/thoughts-on-the-impact-of-rlhf-research). Retrieved 4 March 2023.
  45. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-45)** Belenguer, Lorenzo (2022). ["AI bias: exploring discriminatory algorithmic decision-making models and the application of possible machine-centric solutions adapted from the pharmaceutical industry"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8830968). _AI and Ethics_. **2** (4). AI Ethics: 771–787. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/s43681-022-00138-8](https://doi.org/10.1007%2Fs43681-022-00138-8). [PMC](https://en.wikipedia.org/wiki/PMC_\(identifier\) "PMC \(identifier\)") [8830968](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8830968). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID \(identifier\)") [35194591](https://pubmed.ncbi.nlm.nih.gov/35194591).
  46. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-46)** Zhang, Chiyuan; Bengio, Samy; Hardt, Moritz; Recht, Benjamin; Vinyals, Oriol (4 November 2016). ["Understanding deep learning requires rethinking generalization"](https://openreview.net/forum?id=Sy8gdB9xx). International Conference on Learning Representations.
  47. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-47)** Clark, Jack; Amodei, Dario (21 December 2016). ["Faulty reward functions in the wild"](https://openai.com/research/faulty-reward-functions). OpenAI.
  48. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-48)** Lee, Harrison; Phatale, Samrat; Mansoor, Hassan; Lu, Kellie Ren; Mesnard, Thomas; Ferret, Johan; Bishop, Colton; Hall, Ethan; Carbune, Victor; Rastogi, Abhinav (2023-10-13). ["RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback"](https://openreview.net/forum?id=AAxIs3D2ZZ). _ICLR_.
  49. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-49)** Edwards, Benj (2023-05-09). ["AI gains "values" with Anthropic's new Constitutional AI chatbot approach"](https://arstechnica.com/information-technology/2023/05/ai-with-a-moral-compass-anthropic-outlines-constitutional-ai-in-its-claude-chatbot/). _Ars Technica_. Retrieved 2024-04-27.
  50. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-50)** Rafailov, Rafael; Chittepu, Yaswanth; Park, Ryan; Sikchi, Harshit; Hejna, Joey; Knox, Bradley; Finn, Chelsea; Niekum, Scott (2024). "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2406.02900](https://arxiv.org/abs/2406.02900) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  51. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-51)** Shi, Zhengyan; Land, Sander; Locatelli, Acyr; Geist, Matthieu; Bartolo, Max (2024). "Understanding Likelihood Over-optimisation in Direct Alignment Algorithms". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2410.11677](https://arxiv.org/abs/2410.11677) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  52. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-:12_52-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-:12_52-1) Rafailov, Rafael; Sharma, Archit; Mitchell, Eric; Ermon, Stefano; Manning, Christopher D.; Finn, Chelsea (2023). "Direct Preference Optimization: Your Language Model is Secretly a Reward Model". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2305.18290](https://arxiv.org/abs/2305.18290) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  53. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-53)** Wang, Zhilin; Dong, Yi; Zeng, Jiaqi; Adams, Virginia; Sreedhar, Makesh Narsimhan; Egert, Daniel; Delalleau, Olivier; Scowcroft, Jane Polak; Kant, Neel; Swope, Aidan; Kuchaiev, Oleksii (2023). "HelpSteer: Multi-attribute Helpfulness Dataset for SteerLM". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2311.09528](https://arxiv.org/abs/2311.09528) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  54. ^ [_**a**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-:22_54-0) [_**b**_](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-:22_54-1) Mohammad Gheshlaghi Azar; Rowland, Mark; Piot, Bilal; Guo, Daniel; Calandriello, Daniele; Valko, Michal; Munos, Rémi (2023). "A General Theoretical Paradigm to Understand Learning from Human Preferences". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2310.12036](https://arxiv.org/abs/2310.12036) [[cs.AI](https://arxiv.org/archive/cs.AI)].
  55. **[^](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback#cite_ref-55)** Ethayarajh, Kawin; Xu, Winnie; Muennighoff, Niklas; Jurafsky, Dan; Kiela, Douwe (2024). "KTO: Model Alignment as Prospect Theoretic Optimization". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2402.01306](https://arxiv.org/abs/2402.01306) [[cs.LG](https://arxiv.org/archive/cs.LG)].


## Further reading
[[edit](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&action=edit&section=18 "Edit section: Further reading")]
  * ["Deep reinforcement learning from human preferences"](https://arxiv.org/abs/1706.03741). _NeurIPS_. 2017.
  * ["Training language models to follow instructions with human feedback"](https://arxiv.org/abs/2203.02155). _NeurIPS_. 2022.
  * ["The N Implementation Details of RLHF with PPO"](https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo). _huggingface.co_. 2023-10-24.
  * ["Proximal Policy Optimization — Spinning Up documentation"](https://spinningup.openai.com/en/latest/algorithms/ppo.html). _spinningup.openai.com_. Retrieved 2025-01-26.
  * ["The N+ Implementation Details of RLHF with PPO: A Case Study on TL;DR Summarization"](https://arxiv.org/abs/2403.17031). _COLM_. 2024.

  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Artificial_intelligence_navbox "Template:Artificial intelligence navbox")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Artificial_intelligence_navbox "Template talk:Artificial intelligence navbox")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Artificial_intelligence_navbox "Special:EditPage/Template:Artificial intelligence navbox")

[Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence "Artificial intelligence") (AI)  |  
| --- |  
| 
  * [History](https://en.wikipedia.org/wiki/History_of_artificial_intelligence "History of artificial intelligence")
    * [timeline](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence "Timeline of artificial intelligence")
  * [Glossary](https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence "Glossary of artificial intelligence")
  * [Companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies "List of artificial intelligence companies")
  * [Projects](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_projects "List of artificial intelligence projects")
  * [List of open-source AI software](https://en.wikipedia.org/wiki/Lists_of_open-source_artificial_intelligence_software "Lists of open-source artificial intelligence software")

 |  
| Concepts  | 
  * [Automated reasoning](https://en.wikipedia.org/wiki/Automated_reasoning "Automated reasoning")
  * [Parameter](https://en.wikipedia.org/wiki/Parameter "Parameter")
    * [Hyperparameter](https://en.wikipedia.org/wiki/Hyperparameter_\(machine_learning\) "Hyperparameter \(machine learning\)")
  * [Loss functions](https://en.wikipedia.org/wiki/Loss_functions_for_classification "Loss functions for classification")
  * [Regression](https://en.wikipedia.org/wiki/Regression_analysis "Regression analysis")
    * [Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff "Bias–variance tradeoff")
    * [Double descent](https://en.wikipedia.org/wiki/Double_descent "Double descent")
    * [Overfitting](https://en.wikipedia.org/wiki/Overfitting "Overfitting")
  * [Clustering](https://en.wikipedia.org/wiki/Cluster_analysis "Cluster analysis")
  * [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent "Gradient descent")
    * [SGD](https://en.wikipedia.org/wiki/Stochastic_gradient_descent "Stochastic gradient descent")
    * [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method "Quasi-Newton method")
    * [Conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method "Conjugate gradient method")
  * [Backpropagation](https://en.wikipedia.org/wiki/Backpropagation "Backpropagation")
  * [Attention](https://en.wikipedia.org/wiki/Attention_\(machine_learning\) "Attention \(machine learning\)")
  * [Convolution](https://en.wikipedia.org/wiki/Convolution "Convolution")
  * [Normalization](https://en.wikipedia.org/wiki/Normalization_\(machine_learning\) "Normalization \(machine learning\)")
    * [Batchnorm](https://en.wikipedia.org/wiki/Batch_normalization "Batch normalization")
  * [Activation](https://en.wikipedia.org/wiki/Activation_function "Activation function")
    * [Softmax](https://en.wikipedia.org/wiki/Softmax_function "Softmax function")
    * [Sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function "Sigmoid function")
    * [Rectifier](https://en.wikipedia.org/wiki/Rectifier_\(neural_networks\) "Rectifier \(neural networks\)")
  * [Gating](https://en.wikipedia.org/wiki/Gating_mechanism "Gating mechanism")
  * [Weight initialization](https://en.wikipedia.org/wiki/Weight_initialization "Weight initialization")
  * [Regularization](https://en.wikipedia.org/wiki/Regularization_\(mathematics\) "Regularization \(mathematics\)")
  * [Datasets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets "Training, validation, and test data sets")
    * [Augmentation](https://en.wikipedia.org/wiki/Data_augmentation "Data augmentation")
  * [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering")
  * [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning")
    * [Q-learning](https://en.wikipedia.org/wiki/Q-learning "Q-learning")
    * [SARSA](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action "State–action–reward–state–action")
    * [Imitation](https://en.wikipedia.org/wiki/Imitation_learning "Imitation learning")
    * [Policy gradient](https://en.wikipedia.org/wiki/Policy_gradient_method "Policy gradient method")
  * [Diffusion](https://en.wikipedia.org/wiki/Diffusion_process "Diffusion process")
  * [Latent diffusion model](https://en.wikipedia.org/wiki/Latent_diffusion_model "Latent diffusion model")
  * [Autoregression](https://en.wikipedia.org/wiki/Autoregressive_model "Autoregressive model")
  * [Adversary](https://en.wikipedia.org/wiki/Adversarial_machine_learning "Adversarial machine learning")
  * [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation "Retrieval-augmented generation")
  * [Uncanny valley](https://en.wikipedia.org/wiki/Uncanny_valley "Uncanny valley")
  * RLHF
  * [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning")
  * [Reflection](https://en.wikipedia.org/wiki/Reflection_\(artificial_intelligence\) "Reflection \(artificial intelligence\)")
  * [Recursive self-improvement](https://en.wikipedia.org/wiki/Recursive_self-improvement "Recursive self-improvement")
  * [Hallucination](https://en.wikipedia.org/wiki/Hallucination_\(artificial_intelligence\) "Hallucination \(artificial intelligence\)")
  * [Word embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding")
  * [Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding "Vibe coding")
  * [Symbolic AI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence "Symbolic artificial intelligence")

 |  
| [Applications](https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence "Applications of artificial intelligence")  | 
  * [Automated theorem proving](https://en.wikipedia.org/wiki/Automated_theorem_proving "Automated theorem proving")
  * [Machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning")
    * [In-context learning](https://en.wikipedia.org/wiki/Prompt_engineering#In-context_learning "Prompt engineering")
  * [Artificial neural network](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\) "Neural network \(machine learning\)")
    * [Deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning")
  * [Language model](https://en.wikipedia.org/wiki/Language_model "Language model")
    * [Large](https://en.wikipedia.org/wiki/Large_language_model "Large language model")
    * [NMT](https://en.wikipedia.org/wiki/Neural_machine_translation "Neural machine translation")
    * [Reasoning](https://en.wikipedia.org/wiki/Reasoning_model "Reasoning model")
  * [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol "Model Context Protocol")
  * [Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent "Intelligent agent")
    * [AI agent](https://en.wikipedia.org/wiki/AI_agent "AI agent")
  * [Artificial human companion](https://en.wikipedia.org/wiki/Artificial_human_companion "Artificial human companion")
  * [Humanity's Last Exam](https://en.wikipedia.org/wiki/Humanity%27s_Last_Exam "Humanity's Last Exam")
  * [Lethal autonomous weapons (LAWs)](https://en.wikipedia.org/wiki/Lethal_autonomous_weapon "Lethal autonomous weapon")
  * [Generative AI](https://en.wikipedia.org/wiki/Generative_AI "Generative AI")
  * [Weak AI](https://en.wikipedia.org/wiki/Weak_artificial_intelligence "Weak artificial intelligence")
  * Hypothetical 
    * [Artificial general intelligence (AGI)](https://en.wikipedia.org/wiki/Artificial_general_intelligence "Artificial general intelligence")
    * [Artificial superintelligence (ASI)](https://en.wikipedia.org/wiki/Artificial_superintelligence "Artificial superintelligence")
  * [Agent2Agent protocol](https://en.wikipedia.org/wiki/Agent2Agent "Agent2Agent")

 |  
| Implementations  |   
 | Audio–visual  | 
  * [AlexNet](https://en.wikipedia.org/wiki/AlexNet "AlexNet")
  * [WaveNet](https://en.wikipedia.org/wiki/WaveNet "WaveNet")
  * [Human image synthesis](https://en.wikipedia.org/wiki/Human_image_synthesis "Human image synthesis")
  * [HWR](https://en.wikipedia.org/wiki/Handwriting_recognition "Handwriting recognition")
  * [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition "Optical character recognition")
  * [Computer vision](https://en.wikipedia.org/wiki/Computer_vision "Computer vision")
  * [Speech synthesis](https://en.wikipedia.org/wiki/Deep_learning_speech_synthesis "Deep learning speech synthesis")
    * [15.ai](https://en.wikipedia.org/wiki/15.ai "15.ai")
    * [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs "ElevenLabs")
  * [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition "Speech recognition")
    * [Whisper](https://en.wikipedia.org/wiki/Whisper_\(speech_recognition_system\) "Whisper \(speech recognition system\)")
  * [Facial recognition](https://en.wikipedia.org/wiki/Facial_recognition_system "Facial recognition system")
  * [AlphaFold](https://en.wikipedia.org/wiki/AlphaFold "AlphaFold")
  * [Text-to-image models](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model")
    * [Aurora](https://en.wikipedia.org/wiki/Aurora_\(text-to-image_model\) "Aurora \(text-to-image model\)")
    * [DALL-E](https://en.wikipedia.org/wiki/DALL-E "DALL-E")
    * [Firefly](https://en.wikipedia.org/wiki/Adobe_Firefly "Adobe Firefly")
    * [Flux](https://en.wikipedia.org/wiki/Flux_\(text-to-image_model\) "Flux \(text-to-image model\)")
    * [GPT Image](https://en.wikipedia.org/wiki/GPT_Image "GPT Image")
    * [Ideogram](https://en.wikipedia.org/wiki/Ideogram_\(text-to-image_model\) "Ideogram \(text-to-image model\)")
    * [Imagen](https://en.wikipedia.org/wiki/Imagen_\(text-to-image_model\) "Imagen \(text-to-image model\)")
    * [Midjourney](https://en.wikipedia.org/wiki/Midjourney "Midjourney")
    * [Recraft](https://en.wikipedia.org/wiki/Recraft "Recraft")
    * [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion "Stable Diffusion")
  * [Text-to-video models](https://en.wikipedia.org/wiki/Text-to-video_model "Text-to-video model")
    * [Dream Machine](https://en.wikipedia.org/wiki/Dream_Machine_\(text-to-video_model\) "Dream Machine \(text-to-video model\)")
    * [Runway Gen](https://en.wikipedia.org/wiki/Runway_\(company\)#Services_and_technologies "Runway \(company\)")
    * [Hailuo AI](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Hailuo_AI "MiniMax \(company\)")
    * [Kling](https://en.wikipedia.org/wiki/Kling_AI "Kling AI")
    * [Sora](https://en.wikipedia.org/wiki/Sora_\(text-to-video_model\) "Sora \(text-to-video model\)")
    * [Seedance](https://en.wikipedia.org/wiki/Seedance_2.0 "Seedance 2.0")
    * [Veo](https://en.wikipedia.org/wiki/Veo_\(text-to-video_model\) "Veo \(text-to-video model\)")
  * [Music generation](https://en.wikipedia.org/wiki/Artificial_intelligence_in_music "Artificial intelligence in music")
    * [Riffusion](https://en.wikipedia.org/wiki/Riffusion "Riffusion")
    * [Suno](https://en.wikipedia.org/wiki/Suno_\(platform\) "Suno \(platform\)")
    * [Udio](https://en.wikipedia.org/wiki/Udio "Udio")
  * [World models](https://en.wikipedia.org/wiki/World_model_\(artificial_intelligence\) "World model \(artificial intelligence\)")
    * [Genie](https://en.wikipedia.org/wiki/Genie_\(world_model\) "Genie \(world model\)")
    * [_Oasis_](https://en.wikipedia.org/wiki/Oasis_\(Minecraft_clone\) "Oasis \(Minecraft clone\)")

 |  
| --- | --- |  
| Text  | 
  * [List of large language models](https://en.wikipedia.org/wiki/List_of_large_language_models "List of large language models")
  * [Project Debater](https://en.wikipedia.org/wiki/Project_Debater "Project Debater")
  * [IBM Watson](https://en.wikipedia.org/wiki/IBM_Watson "IBM Watson")
    * [IBM Watsonx](https://en.wikipedia.org/wiki/IBM_Watsonx "IBM Watsonx")

 |  
| Decisional  | 
  * [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo "AlphaGo")
  * [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero "AlphaZero")
  * [OpenAI Five](https://en.wikipedia.org/wiki/OpenAI_Five "OpenAI Five")
  * [Self-driving car](https://en.wikipedia.org/wiki/Self-driving_car "Self-driving car")
  * [MuZero](https://en.wikipedia.org/wiki/MuZero "MuZero")
  * [Action selection](https://en.wikipedia.org/wiki/Action_selection "Action selection")
    * [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT "AutoGPT")
  * [Robot control](https://en.wikipedia.org/wiki/Robot_control "Robot control")

 |  
| [Reasoning systems](https://en.wikipedia.org/wiki/Reasoning_system "Reasoning system")  | 
  * [Deductive classifiers](https://en.wikipedia.org/wiki/Deductive_classifier "Deductive classifier")
  * [Expert systems](https://en.wikipedia.org/wiki/Expert_system "Expert system")
  * [Inference engines](https://en.wikipedia.org/wiki/Inference_engine "Inference engine")
  * [Knowledge-based systems](https://en.wikipedia.org/wiki/Knowledge-based_system "Knowledge-based system")
  * [Logic programs](https://en.wikipedia.org/wiki/Logic_program "Logic program")
  * [Procedural reasoning systems](https://en.wikipedia.org/wiki/Procedural_reasoning_system "Procedural reasoning system")
  * [Semantic reasoners](https://en.wikipedia.org/wiki/Semantic_reasoner "Semantic reasoner")
  * [Rule-based systems](https://en.wikipedia.org/wiki/Rule-based_system "Rule-based system")

 |  
 |  
| People  | 
  * [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing "Alan Turing")
  * [Warren Sturgis McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch "Warren Sturgis McCulloch")
  * [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts "Walter Pitts")
  * [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann "John von Neumann")
  * [Christopher D. Manning](https://en.wikipedia.org/wiki/Christopher_D._Manning "Christopher D. Manning")
  * [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon "Claude Shannon")
  * [Shun'ichi Amari](https://en.wikipedia.org/wiki/Shun%27ichi_Amari "Shun'ichi Amari")
  * [Kunihiko Fukushima](https://en.wikipedia.org/wiki/Kunihiko_Fukushima "Kunihiko Fukushima")
  * [Takeo Kanade](https://en.wikipedia.org/wiki/Takeo_Kanade "Takeo Kanade")
  * [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky "Marvin Minsky")
  * [John McCarthy](https://en.wikipedia.org/wiki/John_McCarthy_\(computer_scientist\) "John McCarthy \(computer scientist\)")
  * [Nathaniel Rochester](https://en.wikipedia.org/wiki/Nathaniel_Rochester_\(computer_scientist\) "Nathaniel Rochester \(computer scientist\)")
  * [Allen Newell](https://en.wikipedia.org/wiki/Allen_Newell "Allen Newell")
  * [Cliff Shaw](https://en.wikipedia.org/wiki/Cliff_Shaw "Cliff Shaw")
  * [Herbert A. Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon "Herbert A. Simon")
  * [Oliver Selfridge](https://en.wikipedia.org/wiki/Oliver_Selfridge "Oliver Selfridge")
  * [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt "Frank Rosenblatt")
  * [Bernard Widrow](https://en.wikipedia.org/wiki/Bernard_Widrow "Bernard Widrow")
  * [Joseph Weizenbaum](https://en.wikipedia.org/wiki/Joseph_Weizenbaum "Joseph Weizenbaum")
  * [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert "Seymour Papert")
  * [Seppo Linnainmaa](https://en.wikipedia.org/wiki/Seppo_Linnainmaa "Seppo Linnainmaa")
  * [Paul Werbos](https://en.wikipedia.org/wiki/Paul_Werbos "Paul Werbos")
  * [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton "Geoffrey Hinton")
  * [John Hopfield](https://en.wikipedia.org/wiki/John_Hopfield "John Hopfield")
  * [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")
  * [Yann LeCun](https://en.wikipedia.org/wiki/Yann_LeCun "Yann LeCun")
  * [Yoshua Bengio](https://en.wikipedia.org/wiki/Yoshua_Bengio "Yoshua Bengio")
  * [Lotfi A. Zadeh](https://en.wikipedia.org/wiki/Lotfi_A._Zadeh "Lotfi A. Zadeh")
  * [Stephen Grossberg](https://en.wikipedia.org/wiki/Stephen_Grossberg "Stephen Grossberg")
  * [Alex Graves](https://en.wikipedia.org/wiki/Alex_Graves_\(computer_scientist\) "Alex Graves \(computer scientist\)")
  * [James Goodnight](https://en.wikipedia.org/wiki/James_Goodnight "James Goodnight")
  * [Andrew Ng](https://en.wikipedia.org/wiki/Andrew_Ng "Andrew Ng")
  * [Fei-Fei Li](https://en.wikipedia.org/wiki/Fei-Fei_Li "Fei-Fei Li")
  * [Alex Krizhevsky](https://en.wikipedia.org/wiki/Alex_Krizhevsky "Alex Krizhevsky")
  * [Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever "Ilya Sutskever")
  * [Oriol Vinyals](https://en.wikipedia.org/wiki/Oriol_Vinyals "Oriol Vinyals")
  * [Quoc V. Le](https://en.wikipedia.org/wiki/Quoc_V._Le "Quoc V. Le")
  * [Ian Goodfellow](https://en.wikipedia.org/wiki/Ian_Goodfellow "Ian Goodfellow")
  * [Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis "Demis Hassabis")
  * [David Silver](https://en.wikipedia.org/wiki/David_Silver_\(computer_scientist\) "David Silver \(computer scientist\)")
  * [Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy "Andrej Karpathy")
  * [Ashish Vaswani](https://en.wikipedia.org/wiki/Ashish_Vaswani "Ashish Vaswani")
  * [Noam Shazeer](https://en.wikipedia.org/wiki/Noam_Shazeer "Noam Shazeer")
  * [Aidan Gomez](https://en.wikipedia.org/wiki/Aidan_Gomez "Aidan Gomez")
  * [John Schulman](https://en.wikipedia.org/wiki/John_Schulman "John Schulman")
  * [Mustafa Suleyman](https://en.wikipedia.org/wiki/Mustafa_Suleyman "Mustafa Suleyman")
  * [Jan Leike](https://en.wikipedia.org/wiki/Jan_Leike "Jan Leike")
  * [Daniel Kokotajlo](https://en.wikipedia.org/wiki/Daniel_Kokotajlo_\(researcher\) "Daniel Kokotajlo \(researcher\)")
  * [François Chollet](https://en.wikipedia.org/wiki/Fran%C3%A7ois_Chollet "François Chollet")

 |  
| Architectures  | 
  * [Neural Turing machine](https://en.wikipedia.org/wiki/Neural_Turing_machine "Neural Turing machine")
  * [Differentiable neural computer](https://en.wikipedia.org/wiki/Differentiable_neural_computer "Differentiable neural computer")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning\) "Transformer \(deep learning\)")
    * [Vision transformer (ViT)](https://en.wikipedia.org/wiki/Vision_transformer "Vision transformer")
  * [Recurrent neural network (RNN)](https://en.wikipedia.org/wiki/Recurrent_neural_network "Recurrent neural network")
  * [Long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory "Long short-term memory")
  * [Gated recurrent unit (GRU)](https://en.wikipedia.org/wiki/Gated_recurrent_unit "Gated recurrent unit")
  * [Echo state network](https://en.wikipedia.org/wiki/Echo_state_network "Echo state network")
  * [Multilayer perceptron (MLP)](https://en.wikipedia.org/wiki/Multilayer_perceptron "Multilayer perceptron")
  * [Convolutional neural network (CNN)](https://en.wikipedia.org/wiki/Convolutional_neural_network "Convolutional neural network")
  * [Residual neural network (RNN)](https://en.wikipedia.org/wiki/Residual_neural_network "Residual neural network")
  * [Highway network](https://en.wikipedia.org/wiki/Highway_network "Highway network")
  * [Mamba](https://en.wikipedia.org/wiki/Mamba_\(deep_learning_architecture\) "Mamba \(deep learning architecture\)")
  * [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder "Autoencoder")
  * [Variational autoencoder (VAE)](https://en.wikipedia.org/wiki/Variational_autoencoder "Variational autoencoder")
  * [Generative adversarial network (GAN)](https://en.wikipedia.org/wiki/Generative_adversarial_network "Generative adversarial network")
  * [Graph neural network (GNN)](https://en.wikipedia.org/wiki/Graph_neural_network "Graph neural network")

 |  
| Political  | 
  * [AI Cold War](https://en.wikipedia.org/wiki/Artificial_Intelligence_Cold_War "Artificial Intelligence Cold War")
  * [AI safety](https://en.wikipedia.org/wiki/AI_safety "AI safety") ([Alignment](https://en.wikipedia.org/wiki/AI_alignment "AI alignment"))
  * [AI takeover](https://en.wikipedia.org/wiki/AI_takeover "AI takeover")
  * [Elections](https://en.wikipedia.org/wiki/Artificial_intelligence_and_elections "Artificial intelligence and elections")
  * [Ethics of AI](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence "Ethics of artificial intelligence")
  * EU [AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act "Artificial Intelligence Act")
  * [Nationalism](https://en.wikipedia.org/wiki/AI_nationalism "AI nationalism")
  * [Precautionary principle](https://en.wikipedia.org/wiki/Precautionary_principle "Precautionary principle")
  * [Regulation of AI](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence "Regulation of artificial intelligence")
    * [US](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence_in_the_United_States "Regulation of artificial intelligence in the United States")
  * [Virtual politician](https://en.wikipedia.org/wiki/Virtual_politician "Virtual politician")

 |  
| Social and economic  | 
  * [AI boom](https://en.wikipedia.org/wiki/AI_boom "AI boom")
  * [AI bubble](https://en.wikipedia.org/wiki/AI_bubble "AI bubble")
  * [AI data center](https://en.wikipedia.org/wiki/AI_data_center "AI data center")
  * [AI effect](https://en.wikipedia.org/wiki/AI_effect "AI effect")
  * [AI literacy](https://en.wikipedia.org/wiki/AI_literacy "AI literacy")
  * [AI slop](https://en.wikipedia.org/wiki/AI_slop "AI slop")
  * [AI veganism](https://en.wikipedia.org/wiki/AI_veganism "AI veganism")
  * [AI winter](https://en.wikipedia.org/wiki/AI_winter "AI winter")
  * [Anthropomorphism](https://en.wikipedia.org/wiki/AI_anthropomorphism "AI anthropomorphism")
  * [Arms race](https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race "Artificial intelligence arms race")
  * [Competition](https://en.wikipedia.org/wiki/Competition_in_artificial_intelligence "Competition in artificial intelligence")
  * [Environmental impact](https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence "Environmental impact of artificial intelligence")
  * [Explainable AI](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence "Explainable artificial intelligence")
  * [Generative engine optimization](https://en.wikipedia.org/wiki/Generative_engine_optimization "Generative engine optimization")
  * [In architecture](https://en.wikipedia.org/wiki/Artificial_intelligence_in_architecture "Artificial intelligence in architecture")
  * [In education](https://en.wikipedia.org/wiki/Artificial_intelligence_in_education "Artificial intelligence in education")
  * [In fiction](https://en.wikipedia.org/wiki/Artificial_intelligence_in_fiction "Artificial intelligence in fiction")
  * [In healthcare](https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare "Artificial intelligence in healthcare")
    * [Chatbot psychosis](https://en.wikipedia.org/wiki/Chatbot_psychosis "Chatbot psychosis")
  * [In marketing](https://en.wikipedia.org/wiki/Artificial_intelligence_in_marketing "Artificial intelligence in marketing")
  * [In video games](https://en.wikipedia.org/wiki/Artificial_intelligence_in_video_games "Artificial intelligence in video games")
  * [In visual art](https://en.wikipedia.org/wiki/Artificial_intelligence_visual_art "Artificial intelligence visual art")
  * [Military applications](https://en.wikipedia.org/wiki/Military_applications_of_artificial_intelligence "Military applications of artificial intelligence")
    * [AI warfare](https://en.wikipedia.org/wiki/AI_warfare "AI warfare")
  * [Workplace impact](https://en.wikipedia.org/wiki/Workplace_impact_of_artificial_intelligence "Workplace impact of artificial intelligence")

 |  
| 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category](https://en.wikipedia.org/wiki/Category:Artificial_intelligence "Category:Artificial intelligence")

 |  
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&oldid=1354240262](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&oldid=1354240262)"
[Categories](https://en.wikipedia.org/wiki/Help:Category "Help:Category"): 
  * [Reinforcement learning](https://en.wikipedia.org/wiki/Category:Reinforcement_learning "Category:Reinforcement learning")
  * [Language modeling](https://en.wikipedia.org/wiki/Category:Language_modeling "Category:Language modeling")
  * [2017 in artificial intelligence](https://en.wikipedia.org/wiki/Category:2017_in_artificial_intelligence "Category:2017 in artificial intelligence")


Hidden categories: 
  * [Articles with short description](https://en.wikipedia.org/wiki/Category:Articles_with_short_description "Category:Articles with short description")
  * [Short description is different from Wikidata](https://en.wikipedia.org/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
  * [Good articles](https://en.wikipedia.org/wiki/Category:Good_articles "Category:Good articles")
  * [Articles needing additional references from March 2026](https://en.wikipedia.org/wiki/Category:Articles_needing_additional_references_from_March_2026 "Category:Articles needing additional references from March 2026")
  * [All articles needing additional references](https://en.wikipedia.org/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")


  * This page was last edited on 15 May 2026, at 04:36 (UTC).
  * Text is available under the [Creative Commons Attribution-ShareAlike 4.0 License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License "Wikipedia:Text of the Creative Commons Attribution-ShareAlike 4.0 International License"); additional terms may apply. By using this site, you agree to the [Terms of Use](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use "foundation:Special:MyLanguage/Policy:Terms of Use") and [Privacy Policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy "foundation:Special:MyLanguage/Policy:Privacy policy"). Wikipedia® is a registered trademark of the [Wikimedia Foundation, Inc.](https://wikimediafoundation.org/), a non-profit organization.


  * [Privacy policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy)
  * [About Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:About)
  * [Disclaimers](https://en.wikipedia.org/wiki/Wikipedia:General_disclaimer)
  * [Contact Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Contact_us)
  * [Legal & safety contacts](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Legal:Wikimedia_Foundation_Legal_and_Safety_Contact_Information)
  * [Code of Conduct](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct)
  * [Developers](https://developer.wikimedia.org)
  * [Statistics](https://stats.wikimedia.org/#/en.wikipedia.org)
  * [Cookie statement](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement)
  * [Mobile view](https://en.wikipedia.org/w/index.php?title=Reinforcement_learning_from_human_feedback&mobileaction=toggle_view_mobile)


  * [![Wikimedia Foundation](https://en.wikipedia.org/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
  * [![Powered by MediaWiki](https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)


Search
Search
Toggle the table of contents
Reinforcement learning from human feedback
[](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) [](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) [](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) [](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) [](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) [](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) [](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
20 languages [Add topic ](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback)
  *[v]: View this template
  *[t]: Discuss this template
  *[e]: Edit this template
