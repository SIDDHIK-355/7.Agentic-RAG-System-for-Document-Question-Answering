[Jump to content](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#bodyContent)
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
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Fine-tuning+%28deep+learning%29 "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Fine-tuning+%28deep+learning%29 "You're encouraged to log in; however, it's not mandatory. \[o\]")


Personal tools
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Fine-tuning+%28deep+learning%29 "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Fine-tuning+%28deep+learning%29 "You're encouraged to log in; however, it's not mandatory. \[o\]")


## Contents
move to sidebar hide
  * [ (Top) ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\))
  * [ 1 Robustness ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Robustness)
  * [ 2 Variants ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Variants) Toggle Variants subsection
    * [ 2.1 Low-rank adaptation ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Low-rank_adaptation)
    * [ 2.2 Representation fine-tuning ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Representation_fine-tuning)
  * [ 3 Applications ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Applications) Toggle Applications subsection
    * [ 3.1 Natural language processing ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Natural_language_processing)
  * [ 4 Commercial models ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#Commercial_models)
  * [ 5 See also ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#See_also)
  * [ 6 References ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#References)


Toggle the table of contents
# Fine-tuning (deep learning)
17 languages
  * [العربية](https://ar.wikipedia.org/wiki/%D8%B5%D9%82%D9%84_\(%D8%AA%D8%B9%D9%84%D9%85_%D8%A7%D9%84%D8%A2%D9%84%D8%A9\) "صقل \(تعلم الآلة\) – Arabic")
  * [Azərbaycanca](https://az.wikipedia.org/wiki/%C4%B0nc%C9%99_t%C9%99nziml%C9%99m%C9%99_\(d%C9%99rin_%C3%B6yr%C9%99nm%C9%99\) "İncə tənzimləmə \(dərin öyrənmə\) – Azerbaijani")
  * [Català](https://ca.wikipedia.org/wiki/Afinament_\(aprenentatge_profund\) "Afinament \(aprenentatge profund\) – Catalan")
  * [Deutsch](https://de.wikipedia.org/wiki/Fine-Tuning_\(K%C3%BCnstliche_Intelligenz\) "Fine-Tuning \(Künstliche Intelligenz\) – German")
  * [Español](https://es.wikipedia.org/wiki/Ajuste_fino_\(aprendizaje_profundo\) "Ajuste fino \(aprendizaje profundo\) – Spanish")
  * [فارسی](https://fa.wikipedia.org/wiki/%D8%AA%D9%86%D8%B8%DB%8C%D9%85_%D8%AF%D9%82%DB%8C%D9%82_\(%DB%8C%D8%A7%D8%AF%DA%AF%DB%8C%D8%B1%DB%8C_%D9%85%D8%A7%D8%B4%DB%8C%D9%86\) "تنظیم دقیق \(یادگیری ماشین\) – Persian")
  * [Français](https://fr.wikipedia.org/wiki/R%C3%A9glage_fin "Réglage fin – French")
  * [עברית](https://he.wikipedia.org/wiki/%D7%9B%D7%95%D7%95%D7%A0%D7%95%D7%9F_%D7%A2%D7%93%D7%99%D7%9F_\(%D7%9C%D7%9E%D7%99%D7%93%D7%94_%D7%A2%D7%9E%D7%95%D7%A7%D7%94\) "כוונון עדין \(למידה עמוקה\) – Hebrew")
  * [Italiano](https://it.wikipedia.org/wiki/Fine-tuning_\(deep_learning\) "Fine-tuning \(deep learning\) – Italian")
  * [日本語](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%B3%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0_\(%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92\) "ファインチューニング \(機械学習\) – Japanese")
  * [한국어](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B8_%ED%8A%9C%EB%8B%9D "파인 튜닝 – Korean")
  * [Polski](https://pl.wikipedia.org/wiki/Dostrajanie_\(sztuczna_inteligencja\) "Dostrajanie \(sztuczna inteligencja\) – Polish")
  * [Português](https://pt.wikipedia.org/wiki/Fine-tuning_\(aprendizado_profundo\) "Fine-tuning \(aprendizado profundo\) – Portuguese")
  * [ไทย](https://th.wikipedia.org/wiki/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%A5%E0%B8%B0%E0%B9%80%E0%B8%AD%E0%B8%B5%E0%B8%A2%E0%B8%94 "การปรับละเอียด – Thai")
  * [Українська](https://uk.wikipedia.org/wiki/%D0%A2%D0%BE%D0%BD%D0%BA%D0%B5_%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D1%8E%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F_\(%D0%B3%D0%BB%D0%B8%D0%B1%D0%BE%D0%BA%D0%B5_%D0%BD%D0%B0%D0%B2%D1%87%D0%B0%D0%BD%D0%BD%D1%8F\) "Тонке настроювання \(глибоке навчання\) – Ukrainian")
  * [粵語](https://zh-yue.wikipedia.org/wiki/%E5%BE%AE%E8%AA%BF_\(%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92\) "微調 \(深度學習\) – Cantonese")
  * [中文](https://zh.wikipedia.org/wiki/%E5%BE%AE%E8%B0%83_\(%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0\) "微调 \(深度学习\) – Chinese")


[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q117286419#sitelinks-wikipedia "Edit interlanguage links")
  * [Article](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\) "View the content page \[c\]")
  * [Talk](https://en.wikipedia.org/wiki/Talk:Fine-tuning_\(deep_learning\) "Discuss improvements to the content page \[t\]")


English
  * [Read](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\))
  * [Edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=history "Past revisions of this page \[h\]")


Tools
Tools
move to sidebar hide
Actions 
  * [Read](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\))
  * [Edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=history)


General 
  * [What links here](https://en.wikipedia.org/wiki/Special:WhatLinksHere/Fine-tuning_\(deep_learning\) "List of all English Wikipedia pages containing links to this page \[j\]")
  * [Related changes](https://en.wikipedia.org/wiki/Special:RecentChangesLinked/Fine-tuning_\(deep_learning\) "Recent changes in pages linked from this page \[k\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files \[u\]")
  * [Permanent link](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&oldid=1358012083 "Permanent link to this revision of this page")
  * [Page information](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=info "More information about this page")
  * [Cite this page](https://en.wikipedia.org/w/index.php?title=Special:CiteThisPage&page=Fine-tuning_%28deep_learning%29&id=1358012083&wpFormIdentifier=titleform "Information on how to cite this page")
  * [Get shortened URL](https://en.wikipedia.org/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFine-tuning_%28deep_learning%29)


Print/export 
  * [Download as PDF](https://en.wikipedia.org/w/index.php?title=Special:DownloadAsPdf&page=Fine-tuning_%28deep_learning%29&action=show-download-screen "Download this page as a PDF file")
  * [Printable version](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&printable=yes "Printable version of this page \[p\]")


In other projects 
  * [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:AI_model_fine-tuning)
  * [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q117286419 "Structured data on this page hosted by Wikidata \[g\]")


Appearance
move to sidebar hide
From Wikipedia, the free encyclopedia
Machine learning technique
In [deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning"), **fine-tuning** is the process of adapting a [computational model](https://en.wikipedia.org/wiki/Computational_model "Computational model") trained for one task (the _upstream task_) to perform a different, usually more specific, task (the _downstream task_).[[1]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-1) It is considered a form of [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning "Transfer learning"), as it reuses knowledge learned from the original training objective.[[2]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-2)[[3]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-3)
Fine-tuning involves applying additional training (e.g., on new data) to the parameters of a [neural network](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\) "Neural network \(machine learning\)") that have been pre-trained.[[4]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-4)[[5]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-d2l-5) Many variants exist. The additional training can be applied to the entire neural network, or to only a subset of its [layers](https://en.wikipedia.org/wiki/Hidden_layers "Hidden layers"), in which case the layers that are not being fine-tuned are "frozen" (i.e., not changed during [backpropagation](https://en.wikipedia.org/wiki/Backpropagation "Backpropagation")).[[6]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-cs231n-6) A model may also be augmented with "adapters"—lightweight modules inserted into the model's architecture that nudge the embedding space for domain adaptation. These contain far fewer parameters than the original model and can be fine-tuned in a parameter-efficient way by tuning only their weights and leaving the rest of the model's weights frozen.[[7]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-7)
For some architectures, such as [convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network "Convolutional neural network"), it is common to keep the earlier layers (those closest to the input layer) frozen, as they capture lower-level [features](https://en.wikipedia.org/wiki/Feature_\(computer_vision\) "Feature \(computer vision\)"), while later layers often discern high-level features that can be more related to the task that the model is trained on.[[6]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-cs231n-6)[[8]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-8)
Models that are pre-trained on large, general corpora are usually fine-tuned by reusing their parameters as a starting point and adding a task-specific layer trained from scratch.[[9]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-9) Fine-tuning the full model is also common and often yields better results, but is more computationally expensive.[[10]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-amazon-10)
Fine-tuning is typically accomplished via [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning"), but there are also techniques to fine-tune a model using [weak supervision](https://en.wikipedia.org/wiki/Semi-supervised_learning "Semi-supervised learning").[[11]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-11) Fine-tuning can be combined with a [reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")-based [objective](https://en.wikipedia.org/wiki/Loss_function "Loss function") to produce language models such as [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT") (a fine-tuned version of [GPT models](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")) and [Sparrow](https://en.wikipedia.org/wiki/Sparrow_\(bot\) "Sparrow \(bot\)").[[12]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-12)[[13]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-13)
## Robustness
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=1 "Edit section: Robustness")]
Fine-tuning can degrade a model's robustness to [distribution shifts](https://en.wikipedia.org/wiki/Domain_adaptation "Domain adaptation").[[14]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-14)[[15]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-15) One mitigation is to linearly interpolate a fine-tuned model's weights with the weights of the original model, which can greatly increase out-of-distribution performance while largely retaining the in-distribution performance of the fine-tuned model.[[16]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-16)
## Variants
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=2 "Edit section: Variants")]
### Low-rank adaptation
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=3 "Edit section: Low-rank adaptation")]
[Low-rank adaptation (LoRA)](https://en.wikipedia.org/wiki/LoRA_\(machine_learning\) "LoRA \(machine learning\)") is an adapter-based technique for efficiently fine-tuning models. The basic idea is to design a low-[rank](https://en.wikipedia.org/wiki/Rank_of_a_matrix "Rank of a matrix") matrix that is then added to the original matrix.[[17]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-17) An adapter, in this context, is a collection of low-rank matrices which, when added to a base model, produces a fine-tuned model. It allows for performance that approaches full-model fine-tuning with lower space requirements. A language model with billions of parameters may be LoRA fine-tuned with only several millions of parameters. 
LoRA-based fine-tuning has become popular in the [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion "Stable Diffusion") community.[[18]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-18) Support for LoRA was integrated into the diffusers library from [Hugging Face](https://en.wikipedia.org/wiki/Hugging_Face "Hugging Face").[[19]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-19) Support for LoRA and similar techniques is also available for a wide range of other models through Hugging Face's _parameter-efficient fine-tuning (PEFT)_ package.[[20]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-20)
### Representation fine-tuning
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=4 "Edit section: Representation fine-tuning")]
Representation fine-tuning (ReFT) is a technique developed by researchers at [Stanford University](https://en.wikipedia.org/wiki/Stanford_University "Stanford University") aimed at fine-tuning large language models (LLMs) by modifying less than 1% of their representations. Unlike parameter-efficient fine-tuning (PEFT) methods, which mainly focus on updating weights, ReFT targets representations. ReFT methods operate on a frozen base model and learn task-specific interventions on hidden representations and train interventions that manipulate a small fraction of model representations to steer model behaviors towards solving downstream tasks at inference time. One specific method within the ReFT family is low-rank linear subspace ReFT (LoReFT), which intervenes on hidden representations in the linear subspace spanned by a low-rank projection matrix. LoReFT can be seen as the representation-based equivalent of low-rank adaptation (LoRA).[[21]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-:0-21)[_[undue weight?](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view#Due_and_undue_weight "Wikipedia:Neutral point of view") – [discuss](https://en.wikipedia.org/wiki/Talk:Fine-tuning_\(deep_learning\)#undue "Talk:Fine-tuning \(deep learning\)")_]
## Applications
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=5 "Edit section: Applications")]
### Natural language processing
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=6 "Edit section: Natural language processing")]
Fine-tuning is common in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") (NLP), especially in the domain of [language modeling](https://en.wikipedia.org/wiki/Language_modeling "Language modeling"). [Large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") like [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI")'s series of [GPT foundation models](https://en.wikipedia.org/wiki/GPT_Foundational_models "GPT Foundational models") can be fine-tuned on data for specific downstream NLP tasks (tasks that use a pre-trained model) to improve performance over the unmodified pre-trained model.[[10]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-amazon-10)
Platforms such as [Semrush](https://en.wikipedia.org/wiki/Semrush "Semrush")'s _AI Visibility Toolkit_ and _Enterprise AIO_ exemplify how fine-tuned models are being used for entity-level monitoring; tracking how named entities are referenced and represented within responses generated by large-language-model-based answer engines.[[22]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-22)
## Commercial models
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=7 "Edit section: Commercial models")]
Commercially-offered large language models can sometimes be fine-tuned if the provider offers a fine-tuning API. As of June 19, 2023, language model fine-tuning APIs are offered by [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") and [Microsoft Azure](https://en.wikipedia.org/wiki/Microsoft_Azure "Microsoft Azure")'s Azure OpenAI Service for a subset of their models, as well as by [Google Cloud Platform](https://en.wikipedia.org/wiki/Google_Cloud_Platform "Google Cloud Platform") for some of their [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM") models, and by others.[[23]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-23)[[24]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-24)[[25]](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_note-25)
## See also
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=8 "Edit section: See also")]
  * [Catastrophic forgetting](https://en.wikipedia.org/wiki/Catastrophic_forgetting "Catastrophic forgetting")
  * [Continual learning](https://en.wikipedia.org/wiki/Continual_learning "Continual learning")
  * [Domain adaptation](https://en.wikipedia.org/wiki/Domain_adaptation "Domain adaptation")
  * [Foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model")
  * [Hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization "Hyperparameter optimization")
  * [Overfitting](https://en.wikipedia.org/wiki/Overfitting "Overfitting")


## References
[[edit](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&action=edit&section=9 "Edit section: References")]
  1. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-1)** von Csefalvay, Chris (2026). "3. Supervised Fine-Tuning: The Foundation Technique.". _Post-Training: A Practical Guide for AI Engineers and Developers_. No Starch Press. pp. 69–101. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-7185-0520-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-7185-0520-9 "Special:BookSources/978-1-7185-0520-9").
  2. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-2)** Botwright, Rob (2024). [_Deep Learning: Computer Vision, Python Machine Learning And Neural Networks_](https://www.google.com/books/edition/Deep_Learning/KpbtEAAAQBAJ?hl=en&gbpv=1&dq=Fine-tuning+deep+learning&pg=PT47&printsec=frontcover). Pastor Publishing Ltd.
  3. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-3)** ABHIJEET, SARKAR. [_Deep Learning Dynamics: The Science Behind AI Training: Exploring the Strategies, Challenges, and Innovations Shaping Modern AI Development Kindle Edition_](https://www.google.com/books/edition/Deep_Learning_Dynamics_The_Science_Behin/cao8EQAAQBAJ?hl=en&gbpv=1&dq=Fine-tuning+deep+learning&pg=PT224&printsec=frontcover).
  4. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-4)** Menshawy, Ahmed (2018). [_Deep Learning By Example: A hands-on guide to implementing advanced machine learning algorithms and neural networks_](https://www.google.com/books/edition/Deep_Learning_By_Example/oulODwAAQBAJ?hl=en&gbpv=1&dq=Fine-tuning+deep+learning&pg=PA233&printsec=frontcover). Packt Publishing. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1788395762](https://en.wikipedia.org/wiki/Special:BookSources/978-1788395762 "Special:BookSources/978-1788395762").
  5. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-d2l_5-0)** Quinn, Joanne (2020). [_Dive into deep learning: tools for engagement_](https://d2l.ai/chapter_computer-vision/fine-tuning.html#steps). p. 551. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-5443-6137-6](https://en.wikipedia.org/wiki/Special:BookSources/978-1-5443-6137-6 "Special:BookSources/978-1-5443-6137-6"). [Archived](https://web.archive.org/web/20230110131250/https://d2l.ai/chapter_computer-vision/fine-tuning.html#steps) from the original on January 10, 2023. Retrieved January 10, 2023.
  6. ^ [_**a**_](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-cs231n_6-0) [_**b**_](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-cs231n_6-1) ["CS231n Convolutional Neural Networks for Visual Recognition"](https://cs231n.github.io/transfer-learning/). _cs231n.github.io_. Retrieved 9 March 2023.
  7. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-7)** Liu, Haokun; Tam, Derek; Muqeeth, Mohammed; Mohta, Jay; Huang, Tenghao; Bansal, Mohit; Raffel, Colin A (2022). Koyejo, S.; Mohamed, S.; Agarwal, A.; Belgrave, D.; Cho, K.; Oh, A. (eds.). [_Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning_](https://proceedings.neurips.cc/paper_files/paper/2022/file/0cde695b83bd186c1fd456302888454c-Paper-Conference.pdf) (PDF). Advances in Neural Information Processing Systems. Vol. 35. Curran Associates, Inc. pp. 1950–1965.
  8. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-8)** Zeiler, Matthew D; Fergus, Rob (2013). "Visualizing and Understanding Convolutional Networks". _ECCV_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1311.2901](https://arxiv.org/abs/1311.2901).
  9. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-9)** Dodge, Jesse; Ilharco, Gabriel; Schwartz, Roy; Farhadi, Ali; [Hajishirzi, Hannaneh](https://en.wikipedia.org/wiki/Hanna_Hajishirzi "Hanna Hajishirzi"); Smith, Noah (2020). "Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2002.06305](https://arxiv.org/abs/2002.06305).`{{cite journal[](https://en.wikipedia.org/wiki/Template:Cite_journal "Template:Cite journal")}}`: Cite journal requires `|journal=` ([help](https://en.wikipedia.org/wiki/Help:CS1_errors#missing_periodical "Help:CS1 errors"))
  10. ^ [_**a**_](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-amazon_10-0) [_**b**_](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-amazon_10-1) Dingliwal, Saket; Shenoy, Ashish; Bodapati, Sravan; Gandhe, Ankur; Gadde, Ravi Teja; Kirchhoff, Katrin (2021). "Prompt Tuning GPT-2 language model for parameter-efficient domain adaptation of ASR systems". _InterSpeech_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2112.08718](https://arxiv.org/abs/2112.08718).
  11. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-11)** Yu, Yue; Zuo, Simiao; Jiang, Haoming; Ren, Wendi; Zhao, Tuo; Zhang, Chao (2020). "Fine-Tuning Pre-trained Language Model with Weak Supervision: A Contrastive-Regularized Self-Training Approach". _Association for Computational Linguistics_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2010.07835](https://arxiv.org/abs/2010.07835).
  12. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-12)** ["Introducing ChatGPT"](https://openai.com/blog/chatgpt). _openai.com_. Retrieved 9 March 2023.
  13. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-13)** Glaese, Amelia; McAleese, Nat; Trębacz, Maja; Aslanides, John; Firoiu, Vlad; Ewalds, Timo; Rauh, Maribeth; Weidinger, Laura; Chadwick, Martin; Thacker, Phoebe; Campbell-Gillingham, Lucy; Uesato, Jonathan; Huang, Po-Sen; Comanescu, Ramona; Yang, Fan; See, Abigail; Dathathri, Sumanth; Greig, Rory; Chen, Charlie; Fritz, Doug; Elias, Jaume Sanchez; Green, Richard; Mokrá, Soňa; Fernando, Nicholas; Wu, Boxi; Foley, Rachel; Young, Susannah; Gabriel, Iason; Isaac, William; Mellor, John; Hassabis, Demis; Kavukcuoglu, Koray; Hendricks, Lisa Anne; Irving, Geoffrey (2022). "Improving alignment of dialogue agents via targeted human judgements". _DeepMind_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2209.14375](https://arxiv.org/abs/2209.14375).
  14. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-14)** Radford, Alec; Kim, Jong Wook; Hallacy, Chris; Ramesh, Aditya; Goh, Gabriel; Agarwal, Sandhini; Sastry, Girish; Askell, Amanda; Mishkin, Pamela; Clark, Jack; Krueger, Gretchen; Sutskever, Ilya (2021). "Learning Transferable Visual Models From Natural Language Supervision". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2103.00020](https://arxiv.org/abs/2103.00020) [[cs.CV](https://arxiv.org/archive/cs.CV)].
  15. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-15)** Kumar, Ananya; Raghunathan, Aditi; Jones, Robbie; Ma, Tengyu; [Liang, Percy](https://en.wikipedia.org/wiki/Percy_Liang "Percy Liang") (2022). "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution". _ICLR_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2202.10054](https://arxiv.org/abs/2202.10054).
  16. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-16)** Wortsman, Mitchell; Ilharco, Gabriel; Kim, Jong Wook; Li, Mike; Kornblith, Simon; Roelofs, Rebecca; Gontijo-Lopes, Raphael; [Hajishirzi, Hannaneh](https://en.wikipedia.org/wiki/Hanna_Hajishirzi "Hanna Hajishirzi"); Farhadi, Ali; Namkoong, Hongseok; Schmidt, Ludwig (2022). "Robust fine-tuning of zero-shot models". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2109.01903](https://arxiv.org/abs/2109.01903) [[cs.CV](https://arxiv.org/archive/cs.CV)].
  17. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-17)** Hu, Edward J.; Shen, Yelong; Wallis, Phillip; Allen-Zhu, Zeyuan; Li, Yuanzhi; Wang, Shean; Wang, Lu; Chen, Weizhu (2022-01-28). ["LoRA: Low-Rank Adaptation of Large Language Models"](https://openreview.net/forum?id=nZeVKeeFYf9). _ICLR_. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2106.09685](https://arxiv.org/abs/2106.09685).
  18. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-18)** Ryu, Simo (February 13, 2023). ["Using Low-rank adaptation to quickly fine-tune diffusion models"](https://github.com/cloneofsimo/lora). _GitHub_. Retrieved June 19, 2023.
  19. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-19)** Cuenca, Pedro; Paul, Sayak (January 26, 2023). ["Using LoRA for Efficient Stable Diffusion Fine-Tuning"](https://huggingface.co/blog/lora). _Hugging Face_. Retrieved June 19, 2023.
  20. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-20)** ["Parameter-Efficient Fine-Tuning using 🤗 PEFT"](https://huggingface.co/blog/peft). _huggingface.co_. Retrieved 2023-06-20.
  21. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-:0_21-0)** Wu, Zhengxuan; Arora, Aryaman; Wang, Zheng; Geiger, Atticus; Jurafsky, Dan; Manning, Christopher D.; Potts, Christopher (2024-04-07), _ReFT: Representation Finetuning for Language Models_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2404.03592](https://arxiv.org/abs/2404.03592)
  22. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-22)** ["Brands target AI chatbots as users switch from Google search"](https://www.ft.com/content/9cc6cc0b-759f-4b8e-9ed1-9e32ad0fe22f?utm). _Financial Times_.
  23. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-23)** ["Fine-tuning"](https://platform.openai.com/docs/guides/fine-tuning). OpenAI. Retrieved 2023-06-19.
  24. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-24)** ["Learn how to customize a model for your application"](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/fine-tuning). Microsoft. Retrieved 2023-06-19.
  25. **[^](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)#cite_ref-25)** ["Tune text foundation models"](https://cloud.google.com/vertex-ai/docs/generative-ai/models/tune-models). Retrieved 2023-06-19.

  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Generative_AI "Template:Generative AI")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Generative_AI "Template talk:Generative AI")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Generative_AI "Special:EditPage/Template:Generative AI")

[Generative AI](https://en.wikipedia.org/wiki/Generative_AI "Generative AI")  |  
| --- |  
| Concepts  | 
  * [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder "Autoencoder")
  * [Deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning")
  * Fine-tuning
  * [Foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model")
  * [Generative adversarial network](https://en.wikipedia.org/wiki/Generative_adversarial_network "Generative adversarial network")
  * [Generative pre-trained transformer](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
  * [Large language model](https://en.wikipedia.org/wiki/Large_language_model "Large language model")
  * [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol "Model Context Protocol")
  * [Neural network](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\) "Neural network \(machine learning\)")
  * [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering")
  * [Reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")
  * [Retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation "Retrieval-augmented generation")
  * [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning")
  * [Stochastic parrot](https://en.wikipedia.org/wiki/Stochastic_parrot "Stochastic parrot")
  * [Synthetic data](https://en.wikipedia.org/wiki/Synthetic_data "Synthetic data")
  * [Top-p sampling](https://en.wikipedia.org/wiki/Top-p_sampling "Top-p sampling")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning\) "Transformer \(deep learning\)")
  * [Variational autoencoder](https://en.wikipedia.org/wiki/Variational_autoencoder "Variational autoencoder")
  * [Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding "Vibe coding")
  * [Vision transformer](https://en.wikipedia.org/wiki/Vision_transformer "Vision transformer")
  * [Word embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding")

 |  
| Models  |   
 | Text  | 
  * [Amazon Nova](https://en.wikipedia.org/wiki/Amazon_Nova "Amazon Nova")
  * [Character.ai](https://en.wikipedia.org/wiki/Character.ai "Character.ai")
  * [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\) "Claude \(language model\)")
  * [Command](https://en.wikipedia.org/wiki/Cohere#Products "Cohere")
  * [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek_\(chatbot\) "DeepSeek \(chatbot\)")
  * [Doubao](https://en.wikipedia.org/wiki/Doubao "Doubao")
  * [Ernie](https://en.wikipedia.org/wiki/Ernie_Bot "Ernie Bot")
  * [EXAONE](https://en.wikipedia.org/wiki/ESTsoft#Government_project_K-EXAONE "ESTsoft")
  * [Gemini](https://en.wikipedia.org/wiki/Google_Gemini "Google Gemini")
  * [Gemma](https://en.wikipedia.org/wiki/Gemma_\(language_model\) "Gemma \(language model\)")
  * [GLM](https://en.wikipedia.org/wiki/Z.ai#History "Z.ai")
  * [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
    * [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT")
  * [Grok](https://en.wikipedia.org/wiki/Grok_\(chatbot\) "Grok \(chatbot\)")
  * [IBM Granite](https://en.wikipedia.org/wiki/IBM_Granite "IBM Granite")
  * [Kimi](https://en.wikipedia.org/wiki/Kimi_\(chatbot\) "Kimi \(chatbot\)")
  * [MAI](https://en.wikipedia.org/wiki/Microsoft_AI#History "Microsoft AI")
  * [Microsoft Copilot](https://en.wikipedia.org/wiki/Microsoft_Copilot "Microsoft Copilot")
  * [Mistral](https://en.wikipedia.org/wiki/Mistral_AI#Models "Mistral AI")
  * [MiniMax](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")
  * [Muse Spark](https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs#Models "Meta Superintelligence Labs")
  * [Nemotron](https://en.wikipedia.org/wiki/Nemotron "Nemotron")
  * [Perplexity](https://en.wikipedia.org/wiki/Perplexity_AI "Perplexity AI")
  * [Solar](https://en.wikipedia.org/wiki/Upstage_\(company\)#Models "Upstage \(company\)")
  * [Poe](https://en.wikipedia.org/wiki/Quora#Poe "Quora")
  * [HKChat](https://en.wikipedia.org/wiki/HKChat "HKChat")
  * [Qwen](https://en.wikipedia.org/wiki/Qwen "Qwen")
  * [Tencent Hy](https://en.wikipedia.org/wiki/Tencent#2021%E2%80%93present:_Regulatory_scrutiny "Tencent")
  * [Xiaomi MiMo](https://en.wikipedia.org/wiki/Xiaomi_MiMo "Xiaomi MiMo")
  * [You.com](https://en.wikipedia.org/wiki/You.com "You.com")

 |  
| --- | --- |  
| [Image](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model")  | 
  * [Adobe Firefly](https://en.wikipedia.org/wiki/Adobe_Firefly "Adobe Firefly")
  * [Flux](https://en.wikipedia.org/wiki/Flux_\(text-to-image_model\) "Flux \(text-to-image model\)")
  * [GPT Image](https://en.wikipedia.org/wiki/GPT_Image "GPT Image")
  * [Ideogram](https://en.wikipedia.org/wiki/Ideogram_\(text-to-image_model\) "Ideogram \(text-to-image model\)")
  * [Midjourney](https://en.wikipedia.org/wiki/Midjourney "Midjourney")
  * [Nano Banana](https://en.wikipedia.org/wiki/Nano_Banana "Nano Banana")
  * [Recraft](https://en.wikipedia.org/wiki/Recraft "Recraft")
  * [Seedream](https://en.wikipedia.org/wiki/ByteDance#Seedream "ByteDance")
  * [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion "Stable Diffusion")

 |  
| [Video](https://en.wikipedia.org/wiki/Text-to-video_model "Text-to-video model")  | 
  * [Dream Machine](https://en.wikipedia.org/wiki/Dream_Machine_\(text-to-video_model\) "Dream Machine \(text-to-video model\)")
  * [Genie](https://en.wikipedia.org/wiki/Genie_\(world_model\) "Genie \(world model\)")
    * [world model](https://en.wikipedia.org/wiki/World_model_\(artificial_intelligence\) "World model \(artificial intelligence\)")
  * [Hailuo AI](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Hailuo_AI "MiniMax \(company\)")
  * [Kling AI](https://en.wikipedia.org/wiki/Kling_AI "Kling AI")
  * [LTX](https://en.wikipedia.org/wiki/LTX_\(text-to-video_model\) "LTX \(text-to-video model\)")
  * [Runway Gen](https://en.wikipedia.org/wiki/Runway_\(company\)#Services_and_technologies "Runway \(company\)")
  * [Seedance](https://en.wikipedia.org/wiki/Seedance_2.0 "Seedance 2.0")
  * [Sora](https://en.wikipedia.org/wiki/Sora_\(text-to-video_model\) "Sora \(text-to-video model\)")
  * [Veo](https://en.wikipedia.org/wiki/Veo_\(text-to-video_model\) "Veo \(text-to-video model\)")

 |  
| [Speech](https://en.wikipedia.org/wiki/Speech_synthesis#Text-to-speech_systems "Speech synthesis")  | 
  * [15.ai](https://en.wikipedia.org/wiki/15.ai "15.ai")
  * [Eleven](https://en.wikipedia.org/wiki/ElevenLabs#Products "ElevenLabs")
  * [Gemini Speech](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini \(language model\)")
  * [MiniMax Speech](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")

 |  
| [Music](https://en.wikipedia.org/wiki/Artificial_intelligence_in_music "Artificial intelligence in music")  | 
  * [Eleven Music](https://en.wikipedia.org/wiki/ElevenLabs#Products "ElevenLabs")
  * [Endel](https://en.wikipedia.org/wiki/Endel_\(app\) "Endel \(app\)")
  * [MiniMax Music](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")
  * [Riffusion](https://en.wikipedia.org/wiki/Riffusion "Riffusion")
  * [Suno](https://en.wikipedia.org/wiki/Suno_\(platform\) "Suno \(platform\)")
  * [Udio](https://en.wikipedia.org/wiki/Udio "Udio")

 |  
 |  
| Products  |   
 | [Coding tools](https://en.wikipedia.org/wiki/List_of_AI-assisted_software_development_tools "List of AI-assisted software development tools")  | 
  * [Claude Code](https://en.wikipedia.org/wiki/Claude_Code "Claude Code")
  * [Codex](https://en.wikipedia.org/wiki/Codex_\(AI_agent\) "Codex \(AI agent\)")
  * [Cursor](https://en.wikipedia.org/wiki/Cursor_\(code_editor\) "Cursor \(code editor\)")
  * [Devin AI](https://en.wikipedia.org/wiki/Devin_AI "Devin AI")
  * [GitHub Copilot](https://en.wikipedia.org/wiki/GitHub_Copilot "GitHub Copilot")
  * [Google Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity "Google Antigravity")
  * [Replit](https://en.wikipedia.org/wiki/Replit "Replit")

 |  
| --- | --- |  
| [Agents](https://en.wikipedia.org/wiki/AI_agent "AI agent")  | 
  * [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT "AutoGPT")
  * [ChatGPT agent](https://en.wikipedia.org/wiki/ChatGPT_agent "ChatGPT agent")
  * [Claude Cowork](https://en.wikipedia.org/wiki/Claude_Cowork "Claude Cowork")
  * [Gemini Spark](https://en.wikipedia.org/wiki/Gemini_Spark "Gemini Spark")
  * [Manus](https://en.wikipedia.org/wiki/Manus_\(AI_agent\) "Manus \(AI agent\)")
  * [MiniMax Agent](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")
  * [OpenClaw](https://en.wikipedia.org/wiki/OpenClaw "OpenClaw")

 |  
 |  
| Applications  | 
  * [Deepfake](https://en.wikipedia.org/wiki/Deepfake "Deepfake")
    * [audio](https://en.wikipedia.org/wiki/Audio_deepfake "Audio deepfake")
  * [Slop](https://en.wikipedia.org/wiki/AI_slop "AI slop")
    * [slopaganda](https://en.wikipedia.org/wiki/Slopaganda "Slopaganda")

 |  
| [Companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies "List of artificial intelligence companies")  | 
  * [Aleph Alpha](https://en.wikipedia.org/wiki/Aleph_Alpha "Aleph Alpha")
  * [Anthropic](https://en.wikipedia.org/wiki/Anthropic "Anthropic")
  * [Anysphere](https://en.wikipedia.org/wiki/Cursor_\(company\) "Cursor \(company\)")
  * [Baichuan](https://en.wikipedia.org/wiki/Baichuan "Baichuan")
  * [Canva](https://en.wikipedia.org/wiki/Canva "Canva")
  * [Cognition AI](https://en.wikipedia.org/wiki/Cognition_AI "Cognition AI")
  * [Cohere](https://en.wikipedia.org/wiki/Cohere "Cohere")
  * [Contextual AI](https://en.wikipedia.org/wiki/Contextual_AI "Contextual AI")
  * [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek "DeepSeek")
  * [DeepL](https://en.wikipedia.org/wiki/DeepL_Translator "DeepL Translator")
  * [EleutherAI](https://en.wikipedia.org/wiki/EleutherAI "EleutherAI")
  * [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs "ElevenLabs")
  * [Google](https://en.wikipedia.org/wiki/Google "Google")
    * [AI](https://en.wikipedia.org/wiki/Google_AI "Google AI")
    * [DeepMind](https://en.wikipedia.org/wiki/Google_DeepMind "Google DeepMind")
  * [HeyGen](https://en.wikipedia.org/wiki/HeyGen "HeyGen")
  * [Hugging Face](https://en.wikipedia.org/wiki/Hugging_Face "Hugging Face")
  * [Inflection AI](https://en.wikipedia.org/wiki/Inflection_AI "Inflection AI")
  * [Kuaishou](https://en.wikipedia.org/wiki/Kuaishou "Kuaishou")
  * [Lightricks](https://en.wikipedia.org/wiki/Lightricks "Lightricks")
  * [Lovable](https://en.wikipedia.org/wiki/Lovable_\(company\) "Lovable \(company\)")
  * [Luma Labs](https://en.wikipedia.org/wiki/Luma_Labs "Luma Labs")
  * [Meta AI](https://en.wikipedia.org/wiki/Meta_AI "Meta AI")
  * [Meta Superintelligence Labs](https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs "Meta Superintelligence Labs")
  * [Microsoft AI](https://en.wikipedia.org/wiki/Microsoft_AI "Microsoft AI")
  * [MiniMax](https://en.wikipedia.org/wiki/MiniMax_Group "MiniMax Group")
  * [Mistral AI](https://en.wikipedia.org/wiki/Mistral_AI "Mistral AI")
  * [Moonshot AI](https://en.wikipedia.org/wiki/Moonshot_AI "Moonshot AI")
  * [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI")
  * [Perplexity AI](https://en.wikipedia.org/wiki/Perplexity_AI "Perplexity AI")
  * [Runway](https://en.wikipedia.org/wiki/Runway_\(company\) "Runway \(company\)")
  * [Safe Superintelligence](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc. "Safe Superintelligence Inc.")
  * [Sakana AI](https://en.wikipedia.org/wiki/Sakana_AI "Sakana AI")
  * [Salesforce](https://en.wikipedia.org/wiki/Salesforce "Salesforce")
  * [Scale AI](https://en.wikipedia.org/wiki/Scale_AI "Scale AI")
  * [SoundHound AI](https://en.wikipedia.org/wiki/SoundHound_AI "SoundHound AI")
  * [SpaceXAI](https://en.wikipedia.org/wiki/SpaceXAI "SpaceXAI")
  * [Stability AI](https://en.wikipedia.org/wiki/Stability_AI "Stability AI")
  * [StepFun](https://en.wikipedia.org/wiki/StepFun "StepFun")
  * [Synthesia](https://en.wikipedia.org/wiki/Synthesia_\(company\) "Synthesia \(company\)")
  * [Thinking Machines Lab](https://en.wikipedia.org/wiki/Thinking_Machines_Lab "Thinking Machines Lab")
  * [Upstage](https://en.wikipedia.org/wiki/Upstage_\(company\) "Upstage \(company\)")
  * [Xiaomi](https://en.wikipedia.org/wiki/Xiaomi "Xiaomi")
  * [Z.ai](https://en.wikipedia.org/wiki/Z.ai "Z.ai")

 |  
| [Controversies](https://en.wikipedia.org/wiki/Artificial_intelligence_controversies "Artificial intelligence controversies")  | 
  * [Generative AI pornography](https://en.wikipedia.org/wiki/Generative_AI_pornography "Generative AI pornography")
    * [Deepfake pornography](https://en.wikipedia.org/wiki/Deepfake_pornography "Deepfake pornography")
      * [on Grok](https://en.wikipedia.org/wiki/Grok_sexual_deepfake_scandal "Grok sexual deepfake scandal")
      * [of Taylor Swift](https://en.wikipedia.org/wiki/Taylor_Swift_deepfake_pornography_controversy "Taylor Swift deepfake pornography controversy")
  * [Pause Giant AI Experiments](https://en.wikipedia.org/wiki/Pause_Giant_AI_Experiments:_An_Open_Letter "Pause Giant AI Experiments: An Open Letter")
  * [Removal of Sam Altman from OpenAI](https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI "Removal of Sam Altman from OpenAI")
  * [Statement on AI Risk](https://en.wikipedia.org/wiki/Statement_on_AI_Risk "Statement on AI Risk")
  * [Tay (chatbot)](https://en.wikipedia.org/wiki/Tay_\(chatbot\) "Tay \(chatbot\)")
  * _[Théâtre D'opéra Spatial](https://en.wikipedia.org/wiki/Th%C3%A9%C3%A2tre_D%27op%C3%A9ra_Spatial "Théâtre D'opéra Spatial")_
  * [Voiceverse NFT plagiarism](https://en.wikipedia.org/wiki/Voiceverse_NFT_plagiarism_scandal "Voiceverse NFT plagiarism scandal")

 |  
| 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category](https://en.wikipedia.org/wiki/Category:Generative_AI "Category:Generative AI")
  * [![](https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png)](https://en.wikipedia.org/wiki/File:Commons-logo.svg "Commons page") [Commons](https://commons.wikimedia.org/wiki/Category:Generative_artificial_intelligence "commons:Category:Generative artificial intelligence")

 |  
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Fine-tuning_(deep_learning)&oldid=1358012083](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&oldid=1358012083)"
[Categories](https://en.wikipedia.org/wiki/Help:Category "Help:Category"): 
  * [Machine learning](https://en.wikipedia.org/wiki/Category:Machine_learning "Category:Machine learning")
  * [Deep learning](https://en.wikipedia.org/wiki/Category:Deep_learning "Category:Deep learning")


Hidden categories: 
  * [CS1 errors: missing periodical](https://en.wikipedia.org/wiki/Category:CS1_errors:_missing_periodical "Category:CS1 errors: missing periodical")
  * [Articles with short description](https://en.wikipedia.org/wiki/Category:Articles_with_short_description "Category:Articles with short description")
  * [Short description is different from Wikidata](https://en.wikipedia.org/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
  * [Articles with minor POV problems from June 2026](https://en.wikipedia.org/wiki/Category:Articles_with_minor_POV_problems_from_June_2026 "Category:Articles with minor POV problems from June 2026")


  * This page was last edited on 6 June 2026, at 00:56 (UTC).
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
  * [Mobile view](https://en.wikipedia.org/w/index.php?title=Fine-tuning_\(deep_learning\)&mobileaction=toggle_view_mobile)


  * [![Wikimedia Foundation](https://en.wikipedia.org/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
  * [![Powered by MediaWiki](https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)


Search
Search
Toggle the table of contents
Fine-tuning (deep learning)
[](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) [](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) [](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) [](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) [](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) [](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) [](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\))
17 languages [Add topic ](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\))
  *[v]: View this template
  *[t]: Discuss this template
  *[e]: Edit this template
