[Jump to content](https://en.wikipedia.org/wiki/BERT_\(language_model\)#bodyContent)
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
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=BERT+%28language+model%29 "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=BERT+%28language+model%29 "You're encouraged to log in; however, it's not mandatory. \[o\]")


Personal tools
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=BERT+%28language+model%29 "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=BERT+%28language+model%29 "You're encouraged to log in; however, it's not mandatory. \[o\]")


## Contents
move to sidebar hide
  * [ (Top) ](https://en.wikipedia.org/wiki/BERT_\(language_model\))
  * [ 1 Architecture ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Architecture) Toggle Architecture subsection
    * [ 1.1 Embedding ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Embedding)
    * [ 1.2 Architectural family ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Architectural_family)
  * [ 2 Training ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Training) Toggle Training subsection
    * [ 2.1 Pre-training ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Pre-training)
      * [ 2.1.1 Masked language modeling ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Masked_language_modeling)
      * [ 2.1.2 Next sentence prediction ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Next_sentence_prediction)
    * [ 2.2 Fine-tuning ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Fine-tuning)
    * [ 2.3 Cost ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Cost)
  * [ 3 Interpretation ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Interpretation)
  * [ 4 History ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#History)
  * [ 5 Variants ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Variants)
  * [ 6 Notes ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Notes)
  * [ 7 References ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#References)
  * [ 8 Further reading ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#Further_reading)
  * [ 9 External links ](https://en.wikipedia.org/wiki/BERT_\(language_model\)#External_links)


Toggle the table of contents
# BERT (language model)
22 languages
  * [العربية](https://ar.wikipedia.org/wiki/%D8%A8%D9%8A%D8%B1%D8%AA_\(%D9%86%D9%85%D9%88%D8%B0%D8%AC_%D9%84%D8%BA%D9%88%D9%8A\) "بيرت \(نموذج لغوي\) – Arabic")
  * [বাংলা](https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%9F_\(%E0%A6%AD%E0%A6%BE%E0%A6%B7%E0%A6%BE_%E0%A6%AE%E0%A6%A1%E0%A7%87%E0%A6%B2\) "বার্ট \(ভাষা মডেল\) – Bangla")
  * [Català](https://ca.wikipedia.org/wiki/BERT_\(model_de_llenguatge\) "BERT \(model de llenguatge\) – Catalan")
  * [Čeština](https://cs.wikipedia.org/wiki/BERT "BERT – Czech")
  * [Deutsch](https://de.wikipedia.org/wiki/Bidirectional_Encoder_Representations_from_Transformers "Bidirectional Encoder Representations from Transformers – German")
  * [Español](https://es.wikipedia.org/wiki/BERT_\(modelo_de_lenguaje\) "BERT \(modelo de lenguaje\) – Spanish")
  * [Euskara](https://eu.wikipedia.org/wiki/BERT_\(hizkuntz_eredua\) "BERT \(hizkuntz eredua\) – Basque")
  * [فارسی](https://fa.wikipedia.org/wiki/%D8%A8%D8%B1%D8%AA_\(%D9%85%D8%AF%D9%84_%D8%B2%D8%A8%D8%A7%D9%86%DB%8C\) "برت \(مدل زبانی\) – Persian")
  * [Français](https://fr.wikipedia.org/wiki/BERT_\(mod%C3%A8le_de_langage\) "BERT \(modèle de langage\) – French")
  * [Galego](https://gl.wikipedia.org/wiki/BERT_\(modelo_de_linguaxe\) "BERT \(modelo de linguaxe\) – Galician")
  * [עברית](https://he.wikipedia.org/wiki/BERT_\(%D7%9E%D7%95%D7%93%D7%9C_%D7%A9%D7%A4%D7%94\) "BERT \(מודל שפה\) – Hebrew")
  * [हिन्दी](https://hi.wikipedia.org/wiki/%E0%A4%AC%E0%A4%B0%E0%A5%8D%E0%A4%9F_\(%E0%A4%AD%E0%A4%BE%E0%A4%B7%E0%A4%BE_%E0%A4%AE%E0%A5%89%E0%A4%A1%E0%A4%B2\) "बर्ट \(भाषा मॉडल\) – Hindi")
  * [Italiano](https://it.wikipedia.org/wiki/BERT "BERT – Italian")
  * [日本語](https://ja.wikipedia.org/wiki/BERT_\(%E8%A8%80%E8%AA%9E%E3%83%A2%E3%83%87%E3%83%AB\) "BERT \(言語モデル\) – Japanese")
  * [한국어](https://ko.wikipedia.org/wiki/BERT_\(%EC%96%B8%EC%96%B4_%EB%AA%A8%EB%8D%B8\) "BERT \(언어 모델\) – Korean")
  * [Lietuvių](https://lt.wikipedia.org/wiki/BERT "BERT – Lithuanian")
  * [Português](https://pt.wikipedia.org/wiki/BERT_\(modelo_de_linguagem\) "BERT \(modelo de linguagem\) – Portuguese")
  * [Ślůnski](https://szl.wikipedia.org/wiki/BERT "BERT – Silesian")
  * [Українська](https://uk.wikipedia.org/wiki/BERT_\(%D0%BC%D0%BE%D0%B2%D0%BD%D0%B0_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C\) "BERT \(мовна модель\) – Ukrainian")
  * [Tiếng Việt](https://vi.wikipedia.org/wiki/BERT_\(m%C3%B4_h%C3%ACnh_ng%C3%B4n_ng%E1%BB%AF\) "BERT \(mô hình ngôn ngữ\) – Vietnamese")
  * [粵語](https://zh-yue.wikipedia.org/wiki/BERT "BERT – Cantonese")
  * [中文](https://zh.wikipedia.org/wiki/BERT "BERT – Chinese")


[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q61726893#sitelinks-wikipedia "Edit interlanguage links")
  * [Article](https://en.wikipedia.org/wiki/BERT_\(language_model\) "View the content page \[c\]")
  * [Talk](https://en.wikipedia.org/wiki/Talk:BERT_\(language_model\) "Discuss improvements to the content page \[t\]")


English
  * [Read](https://en.wikipedia.org/wiki/BERT_\(language_model\))
  * [Edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=history "Past revisions of this page \[h\]")


Tools
Tools
move to sidebar hide
Actions 
  * [Read](https://en.wikipedia.org/wiki/BERT_\(language_model\))
  * [Edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=history)


General 
  * [What links here](https://en.wikipedia.org/wiki/Special:WhatLinksHere/BERT_\(language_model\) "List of all English Wikipedia pages containing links to this page \[j\]")
  * [Related changes](https://en.wikipedia.org/wiki/Special:RecentChangesLinked/BERT_\(language_model\) "Recent changes in pages linked from this page \[k\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files \[u\]")
  * [Permanent link](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&oldid=1356209197 "Permanent link to this revision of this page")
  * [Page information](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=info "More information about this page")
  * [Cite this page](https://en.wikipedia.org/w/index.php?title=Special:CiteThisPage&page=BERT_%28language_model%29&id=1356209197&wpFormIdentifier=titleform "Information on how to cite this page")
  * [Get shortened URL](https://en.wikipedia.org/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBERT_%28language_model%29)


Print/export 
  * [Download as PDF](https://en.wikipedia.org/w/index.php?title=Special:DownloadAsPdf&page=BERT_%28language_model%29&action=show-download-screen "Download this page as a PDF file")
  * [Printable version](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&printable=yes "Printable version of this page \[p\]")


In other projects 
  * [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:BERT)
  * [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q61726893 "Structured data on this page hosted by Wikidata \[g\]")


Appearance
move to sidebar hide
From Wikipedia, the free encyclopedia
Series of language models developed by Google AI  
| Bidirectional encoder representations from transformers (BERT) |  
| --- |  
| [Original author](https://en.wikipedia.org/wiki/Programmer "Programmer")  | [Google AI](https://en.wikipedia.org/wiki/Google_AI "Google AI")  |  
| Initial release  | October 31, 2018[[1]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-1)  |  
| [Type](https://en.wikipedia.org/wiki/Software_categories#Categorization_approaches "Software categories")  | 
  * [Large language model](https://en.wikipedia.org/wiki/Large_language_model "Large language model")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\) "Transformer \(deep learning architecture\)")
  * [Foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model")

 |  
| [License](https://en.wikipedia.org/wiki/Software_license "Software license")  | [Apache 2.0](https://en.wikipedia.org/wiki/Apache_2.0 "Apache 2.0")  |  
| Website  |  [arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805) [![Edit this on Wikidata](https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png)](https://www.wikidata.org/wiki/Q61726893?uselang=en#P856 "Edit this on Wikidata")  |  
| [Repository](https://en.wikipedia.org/wiki/Repository_\(version_control\) "Repository \(version control\)")  | [github.com/google-research/bert](https://github.com/google-research/bert)  |  
**Bidirectional encoder representations from transformers** (**BERT**) is a [language model](https://en.wikipedia.org/wiki/Language_model "Language model") introduced in October 2018 by researchers at [Google](https://en.wikipedia.org/wiki/Google "Google").[[2]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:0-2)[[3]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-3) It learns to represent text as a sequence of vectors using [self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning"). It uses the [encoder-only transformer](https://en.wikipedia.org/wiki/Transformer_\(machine_learning_model\) "Transformer \(machine learning model\)") architecture. BERT dramatically improved the state of the art for [large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model"). As of 2020[[update]](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit), BERT is a ubiquitous baseline in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") (NLP) experiments.[[4]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:4-4)
BERT is trained by masked token prediction and next sentence prediction. With this training, BERT learns contextual, [latent representations](https://en.wikipedia.org/wiki/Latent_space "Latent space") of tokens in their context, similar to [ELMo](https://en.wikipedia.org/wiki/ELMo "ELMo") and [GPT-2](https://en.wikipedia.org/wiki/GPT-2 "GPT-2").[[5]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:5-5) It found applications for many natural language processing tasks, such as [coreference resolution](https://en.wikipedia.org/wiki/Coreference_resolution "Coreference resolution") and [polysemy](https://en.wikipedia.org/wiki/Polysemy "Polysemy") resolution.[[6]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-6) It improved on [ELMo](https://en.wikipedia.org/wiki/ELMo "ELMo") and spawned the study of "BERTology", which attempts to interpret what is learned by BERT.[[4]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:4-4)
BERT was originally implemented in the English language at two model sizes, BERTBASE (110 million parameters) and BERTLARGE (340 million parameters). Both were trained on the Toronto [BookCorpus](https://en.wikipedia.org/wiki/BookCorpus "BookCorpus")[[7]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-bookcorpus-7) (800M words) and [English Wikipedia](https://en.wikipedia.org/wiki/English_Wikipedia "English Wikipedia") (2,500M words).[[2]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:0-2): 5  The weights were released on [GitHub](https://en.wikipedia.org/wiki/GitHub "GitHub").[[8]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:3-8) On March 11, 2020, 24 smaller models were released, the smallest being BERTTINY with just 4 million parameters.[[8]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:3-8)
## Architecture
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=1 "Edit section: Architecture")]
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/BERT_embeddings_01.png/330px-BERT_embeddings_01.png)](https://en.wikipedia.org/wiki/File:BERT_embeddings_01.png)High-level schematic diagram of BERT. It takes in a text, tokenizes it into a sequence of tokens, add in optional special tokens, and apply a Transformer encoder. The hidden states of the last layer can then be used as contextual word embeddings.
BERT is an "encoder-only" [transformer](https://en.wikipedia.org/wiki/Transformer_\(machine_learning_model\) "Transformer \(machine learning model\)") architecture. At a high level, BERT consists of 4 modules: 
  * Tokenizer: This module converts a piece of English text into a sequence of integers ("tokens").
  * [Embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding"): This module converts the sequence of tokens into an array of real-valued vectors representing the tokens. It represents the conversion of discrete token types into a lower-dimensional [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space").
  * Encoder: a stack of Transformer blocks with [self-attention](https://en.wikipedia.org/wiki/Attention_\(machine_learning\) "Attention \(machine learning\)"), but without causal masking.
  * Task head: This module converts the final representation vectors into one-shot encoded tokens again by producing a predicted probability distribution over the token types. It can be viewed as a simple decoder, decoding the latent representation into token types, or as an "un-embedding layer".


The task head is necessary for pre-training, but it is often unnecessary for so-called "downstream tasks," such as [question answering](https://en.wikipedia.org/wiki/Question_answering "Question answering") or [sentiment classification](https://en.wikipedia.org/wiki/Sentiment_analysis "Sentiment analysis"). Instead, one removes the task head and replaces it with a newly initialized module suited for the task, and finetune the new module. The latent vector representation of the model is directly fed into this new module, allowing for sample-efficient [transfer learning](https://en.wikipedia.org/wiki/Transfer_learning "Transfer learning").[[2]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:0-2)[[9]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-9)
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/BERT_encoder-only_attention.svg/250px-BERT_encoder-only_attention.svg.png)](https://en.wikipedia.org/wiki/File:BERT_encoder-only_attention.svg)Encoder-only attention is all-to-all.
### Embedding
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=2 "Edit section: Embedding")]
This section describes the embedding used by BERTBASE. The other one, BERTLARGE, is similar, just larger. 
The tokenizer of BERT is WordPiece, which is a sub-word strategy like [byte-pair encoding](https://en.wikipedia.org/wiki/Byte-pair_encoding "Byte-pair encoding"). Its vocabulary size is 30,000, and any token not appearing in its vocabulary is replaced by `[UNK]` ("unknown"). 
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/BERT_input_embeddings.png/330px-BERT_input_embeddings.png)](https://en.wikipedia.org/wiki/File:BERT_input_embeddings.png)The three kinds of embedding used by BERT: token type, position, and segment type.
The first layer is the embedding layer, which contains three components: token type embeddings, position embeddings, and segment type embeddings. 
  * Token type: The token type is a standard embedding layer, translating a one-hot vector into a dense vector based on its token type.
  * Position: The position embeddings are based on a token's position in the sequence. BERT uses absolute position embeddings, where each position in a sequence is mapped to a real-valued vector. Each dimension of the vector consists of a [sinusoidal function](https://en.wikipedia.org/wiki/Sine_wave "Sine wave") that takes the position in the sequence as input.
  * Segment type: Using a vocabulary of just 0 or 1, this embedding layer produces a dense vector based on whether the token belongs to the first or second text segment in that input. In other words, type-1 tokens are all tokens that appear after the `[SEP]` special token. All prior tokens are type-0.


The three embedding vectors are added together representing the initial token representation as a function of these three pieces of information. After embedding, the vector representation is normalized using a [LayerNorm](https://en.wikipedia.org/wiki/LayerNorm "LayerNorm") operation, outputting a 768-dimensional vector for each input token. After this, the representation vectors are passed forward through 12 Transformer encoder blocks, and are decoded back to 30,000-dimensional vocabulary space using a basic affine transformation layer. 
### Architectural family
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=3 "Edit section: Architectural family")]
The encoder stack of BERT has 2 free parameters:  L {\displaystyle L} ![{\\displaystyle L}](https://wikimedia.org/api/rest_v1/media/math/render/svg/103168b86f781fe6e9a4a87b8ea1cebe0ad4ede8), the number of layers, and  H {\displaystyle H} ![{\\displaystyle H}](https://wikimedia.org/api/rest_v1/media/math/render/svg/75a9edddcca2f782014371f75dca39d7e13a9c1b), the _hidden size_. There are always  H / 64 {\displaystyle H/64} ![{\\displaystyle H/64}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4851b2f11e580fbfb783e25e2b13fde9f17e75f6) self-attention heads, and the feed-forward/filter size is always  4 H {\displaystyle 4H} ![{\\displaystyle 4H}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1a36a1b004276c3d27d0691f70c990256e2e964b). By varying these two numbers, one obtains an entire family of BERT models.[[10]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-10)
For BERT: 
  * the _feed-forward size_ and _filter size_ are synonymous. Both of them denote the number of dimensions in the middle layer of the feed-forward network.
  * the _hidden size_ and _embedding size_ are synonymous. Both of them denote the number of real numbers used to represent a token.


The notation for encoder stack is written as L/H. For example, BERTBASE is written as 12L/768H, BERTLARGE as 24L/1024H, and BERTTINY as 2L/128H. 
## Training
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=4 "Edit section: Training")]
### Pre-training
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=5 "Edit section: Pre-training")]
BERT was pre-trained simultaneously on two tasks:[[11]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-11)
  * _Masked language modeling_ (MLM): In this task, BERT ingests a sequence of words, where one word may be randomly changed ("masked"), and BERT tries to predict the original words that had been changed. For example, in the sentence "The cat sat on the `[MASK]`," BERT would need to predict "mat." This helps BERT learn bidirectional context, meaning it understands the relationships between words not just from left to right or right to left but from both directions at the same time.


  * _Next sentence prediction_ (NSP): In this task, BERT is trained to predict whether one sentence logically follows another. For example, given two sentences, "The cat sat on the mat" and "It was a sunny day", BERT has to decide if the second sentence is a valid continuation of the first one. This helps BERT understand relationships between sentences, which is important for tasks like question answering or document classification.


#### Masked language modeling
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=6 "Edit section: Masked language modeling")]
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/BERT_masked_language_modelling_task.png/250px-BERT_masked_language_modelling_task.png)](https://en.wikipedia.org/wiki/File:BERT_masked_language_modelling_task.png)The masked language modeling task
In masked language modeling, 15% of tokens would be randomly selected for masked-prediction task, and the training objective was to predict the masked token given its context. In more detail, the selected token is: 
  * replaced with a `[MASK]` token with probability 80%,
  * replaced with a random word token with probability 10%,
  * not replaced with probability 10%.


The reason not all selected tokens are masked is to avoid the dataset shift problem. The dataset shift problem arises when the distribution of inputs seen during training differs significantly from the distribution encountered during inference. A trained BERT model might be applied to word representation (like [Word2Vec](https://en.wikipedia.org/wiki/Word2Vec "Word2Vec")), where it would be run over sentences not containing any `[MASK]` tokens. It is later found that more diverse training objectives are generally better.[[12]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-12)
As an illustrative example, consider the sentence "my dog is cute". It would first be divided into tokens like "my1 dog2 is3 cute4". Then a random token in the sentence would be picked. Let it be the 4th one "cute4". Next, there would be three possibilities: 
  * with probability 80%, the chosen token is masked, resulting in "my1 dog2 is3 `[MASK]`4";
  * with probability 10%, the chosen token is replaced by a uniformly sampled random token, such as "happy", resulting in "my1 dog2 is3 happy4";
  * with probability 10%, nothing is done, resulting in "my1 dog2 is3 cute4".


After processing the input text, the model's 4th output vector is passed to its decoder layer, which outputs a probability distribution over its 30,000-dimensional vocabulary space. 
#### Next sentence prediction
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=7 "Edit section: Next sentence prediction")]
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/BERT_next_sequence_prediction_task.png/250px-BERT_next_sequence_prediction_task.png)](https://en.wikipedia.org/wiki/File:BERT_next_sequence_prediction_task.png)The next sentence prediction task
Given two sentences, the model predicts if they appear sequentially in the training corpus, outputting either `[IsNext]` or `[NotNext]`. During training, the algorithm sometimes samples two sentences from a single continuous span in the training corpus, while at other times, it samples two sentences from two discontinuous spans. 
The first sentence starts with a special token, `[CLS]` (for "classify"). The two sentences are separated by another special token, `[SEP]` (for "separate"). After processing the two sentences, the final vector for the `[CLS]` token is passed to a linear layer for binary classification into `[IsNext]` and `[NotNext]`. 
For example: 
  * Given "`[CLS]` my dog is cute `[SEP]` he likes playing `[SEP]`", the model should predict `[IsNext]`.
  * Given "`[CLS]` my dog is cute `[SEP]` how do magnets work `[SEP]`", the model should predict `[NotNext]`.


### Fine-tuning
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=8 "Edit section: Fine-tuning")]
Fine-tuned tasks for BERT[[13]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-zhangetal2024-13)
  * [![Sentiment classification](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/BERT_on_sentiment_classification.svg/250px-BERT_on_sentiment_classification.svg.png)](https://en.wikipedia.org/wiki/File:BERT_on_sentiment_classification.svg "Sentiment classification")
Sentiment classification
  * [![Sentence classification](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/BERT_on_sentence_classification.svg/250px-BERT_on_sentence_classification.svg.png)](https://en.wikipedia.org/wiki/File:BERT_on_sentence_classification.svg "Sentence classification")
Sentence classification
  * [![Answering multiple-choice questions](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/BERT_on_multiple-choice_question-answering.svg/250px-BERT_on_multiple-choice_question-answering.svg.png)](https://en.wikipedia.org/wiki/File:BERT_on_multiple-choice_question-answering.svg "Answering multiple-choice questions")
Answering multiple-choice questions
  * [![Part-of-speech tagging](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/BERT_on_tagging.svg/250px-BERT_on_tagging.svg.png)](https://en.wikipedia.org/wiki/File:BERT_on_tagging.svg "Part-of-speech tagging")
[Part-of-speech tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging "Part-of-speech tagging")


BERT is meant as a general pretrained model for various applications in natural language processing. That is, after pre-training, BERT can be [fine-tuned](https://en.wikipedia.org/wiki/Fine-tuning_\(machine_learning\) "Fine-tuning \(machine learning\)") with fewer resources on smaller datasets to optimize its performance on specific tasks such as [natural language inference](https://en.wikipedia.org/wiki/Textual_entailment "Textual entailment") and [text classification](https://en.wikipedia.org/wiki/Document_classification "Document classification"), and sequence-to-sequence-based language generation tasks such as [question answering](https://en.wikipedia.org/wiki/Question_answering "Question answering") and conversational response generation.[[13]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-zhangetal2024-13)
The original BERT paper published results demonstrating that a small amount of finetuning (for BERTLARGE, 1 hour on 1 Cloud TPU) allowed it to achieve [state-of-the-art](https://en.wikipedia.org/wiki/State_of_the_art "State of the art") performance on a number of [natural language understanding](https://en.wikipedia.org/wiki/Natural-language_understanding "Natural-language understanding") tasks:[[2]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:0-2)
  * GLUE ([General Language Understanding Evaluation](https://en.wikipedia.org/wiki/General_Language_Understanding_Evaluation "General Language Understanding Evaluation")) task set (consisting of 9 tasks);
  * SQuAD (Stanford Question Answering Dataset[[14]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-14)) v1.1 and v2.0;
  * SWAG (Situations With Adversarial Generations[[15]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-15)).


In the original paper, all parameters of BERT are fine-tuned, and recommended that, for downstream applications that are text classifications, the output token at the `[CLS]` input token is fed into a linear-softmax layer to produce the label outputs.[[2]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:0-2)
The original code base defined the final linear layer as a "pooler layer", in analogy with [global pooling](https://en.wikipedia.org/wiki/Pooling_layer "Pooling layer") in computer vision, even though it simply discards all output tokens except the one corresponding to `[CLS]`.[[16]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-16)
### Cost
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=9 "Edit section: Cost")]
BERT was trained on the [BookCorpus](https://en.wikipedia.org/wiki/BookCorpus "BookCorpus") (800M words) and a filtered version of English Wikipedia (2,500M words) without lists, tables, and headers. 
Training BERTBASE on 4 cloud [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit "Tensor Processing Unit") (16 TPU chips total) took 4 days, at an estimated cost of 500 USD.[[8]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:3-8) Training BERTLARGE on 16 cloud TPU (64 TPU chips total) took 4 days.[[2]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:0-2)
## Interpretation
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=10 "Edit section: Interpretation")]
Language models like ELMo, GPT-2, and BERT, spawned the study of "BERTology", which attempts to interpret what is learned by these models. Their performance on these [natural language understanding](https://en.wikipedia.org/wiki/Natural-language_understanding "Natural-language understanding") tasks are not yet well understood.[[4]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:4-4)[[17]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:1-17)[[18]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:2-18) Several research publications in 2018 and 2019 focused on investigating the relationship behind BERT's output as a result of carefully chosen input sequences,[[19]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-19)[[20]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-20) analysis of internal [vector representations](https://en.wikipedia.org/wiki/Vector_space_model "Vector space model") through probing classifiers,[[21]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-21)[[22]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-22) and the relationships represented by [attention](https://en.wikipedia.org/wiki/Transformer_\(machine_learning_model\)#Architecture "Transformer \(machine learning model\)") weights.[[17]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:1-17)[[18]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:2-18)
The high performance of the BERT model could also be attributed to the fact that it is bidirectionally trained.[[23]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-23) This means that BERT, based on the Transformer model architecture, applies its self-attention mechanism to learn information from a text from the left and right side during training, and consequently gains a deep understanding of the context. For example, the word _fine_ can have two different meanings depending on the context (**I feel** fine **today** , **She has** fine **blond hair**). BERT considers the words surrounding the target word _fine_ from the left and right side. 
However it comes at a cost: due to [encoder-only](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\)#encoder-only "Transformer \(deep learning architecture\)") architecture lacking a decoder, BERT can't [be prompted](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering") and can't [generate text](https://en.wikipedia.org/wiki/Natural_language_generation "Natural language generation"), while bidirectional models in general do not work effectively without the right side, thus being difficult to prompt. As an illustrative example, if one wishes to use BERT to continue a sentence fragment "Today, I went to", then naively one would mask out all the tokens as "Today, I went to `[MASK]` `[MASK]` `[MASK]` ... `[MASK]` ." where the number of `[MASK]` is the length of the sentence one wishes to extend to. However, this constitutes a dataset shift, as during training, BERT has never seen sentences with that many tokens masked out. Consequently, its performance degrades. More sophisticated techniques allow text generation, but at a high computational cost.[[24]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-24)
## History
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=11 "Edit section: History")]
BERT was originally published by Google researchers Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. The design has its origins from pre-training contextual representations, including [semi-supervised sequence learning](https://en.wikipedia.org/wiki/Semi-supervised_learning "Semi-supervised learning"),[[25]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-25) generative pre-training, [ELMo](https://en.wikipedia.org/wiki/ELMo "ELMo"),[[26]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-26) and ULMFit.[[27]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-27) Unlike previous models, BERT is a deeply bidirectional, [unsupervised](https://en.wikipedia.org/wiki/Unsupervised_learning "Unsupervised learning") language representation, pre-trained using only a plain [text corpus](https://en.wikipedia.org/wiki/Text_corpus "Text corpus"). Context-free models such as [word2vec](https://en.wikipedia.org/wiki/Word2vec "Word2vec") or [GloVe](https://en.wikipedia.org/wiki/GloVe_\(machine_learning\) "GloVe \(machine learning\)") generate a single word embedding representation for each word in the vocabulary, whereas BERT takes into account the context for each occurrence of a given word. For instance, whereas the vector for "running" will have the same word2vec vector representation for both of its occurrences in the sentences "He is running a company" and "He is running a marathon", BERT will provide a contextualized embedding that will be different according to the sentence.[[5]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-:5-5)
On October 25, 2019, [Google](https://en.wikipedia.org/wiki/Google "Google") announced that they had started applying BERT models to [English-language](https://en.wikipedia.org/wiki/English-language "English-language") search queries on [Google Search](https://en.wikipedia.org/wiki/Google_Search "Google Search") within the US.[[28]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-28) On December 9, 2019, it was reported that BERT had been adopted by Google Search for over 70 languages.[[29]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-29)[[30]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-30) In October 2020, almost every single English-based query was processed by a BERT model.[[31]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-31)
## Variants
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=12 "Edit section: Variants")]
The BERT models were influential and inspired many variants. 
**RoBERTa** (2019)[[32]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-32) was an engineering improvement. It preserves BERT's architecture (slightly larger, at 355M parameters), but improves its training, changing key hyperparameters, removing the _next-sentence prediction_ task, and using much larger [mini-batch](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Iterative_method "Stochastic gradient descent") sizes. 
**XLM-RoBERTa** (2019)[[33]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-33) was a multilingual RoBERTa model. It was one of the first works on multilingual language modeling at scale. 
**DistilBERT** (2019) [distills](https://en.wikipedia.org/wiki/Knowledge_distillation "Knowledge distillation") BERTBASE to a model with just 60% of its parameters (66M), while preserving 95% of its benchmark scores.[[34]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-34)[[35]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-35) Similarly, **TinyBERT** (2019)[[36]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-36) is a distilled model with just 28% of its parameters. 
**ALBERT** (2019)[[37]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-37) used shared-parameter across layers, and experimented with independently varying the hidden size and the word-embedding layer's output size as two hyperparameters. They also replaced the _next sentence prediction_ task with the _sentence-order prediction_ (SOP) task, where the model must distinguish the correct order of two consecutive text segments from their reversed order. 
**ELECTRA** (2020)[[38]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-38) applied the idea of [generative adversarial networks](https://en.wikipedia.org/wiki/Generative_adversarial_network "Generative adversarial network") to the MLM task. Instead of masking out tokens, a small language model generates random plausible substitutions, and a larger network identify these replaced tokens. The small model aims to fool the large model. 
**DeBERTa** (2020)[[39]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-39) is a significant architectural variant, with _disentangled attention_. Its key idea is to treat the positional and token encodings separately throughout the attention mechanism. Instead of combining the positional encoding ( x p o s i t i o n {\displaystyle x_{\mathrm {position} }} ![{\\displaystyle x_{\\mathrm {position} }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f4c4fae9ddf3fdaf4abfea3d5631a41910988f5a)) and token encoding ( x t o k e n {\displaystyle x_{\mathrm {token} }} ![{\\displaystyle x_{\\mathrm {token} }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6b4a6ec3801e3912d1959e4c1ebb696fbc8b8250)) into a single input vector ( x i n p u t = x p o s i t i o n + x t o k e n {\displaystyle x_{\mathrm {input} }=x_{\mathrm {position} }+x_{\mathrm {token} }} ![{\\displaystyle x_{\\mathrm {input} }=x_{\\mathrm {position} }+x_{\\mathrm {token} }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/059ce939e509fc9169e6a38fd3e78dc6b6b8a3a1)), DeBERTa keeps them separate as a tuple:  ( x p o s i t i o n , x t o k e n ) {\displaystyle (x_{\mathrm {position} },x_{\mathrm {token} })} ![{\\displaystyle \(x_{\\mathrm {position} },x_{\\mathrm {token} }\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9616303e1e24051394ba0aa2a926342956a33e1d). Then, at each self-attention layer, DeBERTa computes three distinct attention matrices, rather than the single attention matrix used in BERT:[[note 1]](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_note-name-40)  
| Attention type   | Query type   | Key type   | Example   |  
| --- | --- | --- | --- |  
| Content-to-content   | Token   | Token   | "European"; "Union", "continent"   |  
| Content-to-position   | Token   | Position   | [adjective]; +1, +2, +3   |  
| Position-to-content   | Position   | Token   | −1; "not", "very"   |  
The three attention matrices are added together element-wise, then passed through a softmax layer and multiplied by a projection matrix. 
Absolute position encoding is included in the final self-attention layer as additional input. 
## Notes
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=13 "Edit section: Notes")]
  1. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-name_40-0)** The position-to-position type was omitted by the authors for being useless.


## References
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=14 "Edit section: References")]
  1. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-1)** ["Initial BERT release · google-research/bert@fe35475"](https://github.com/google-research/bert/commit/fe354751d7de010f60d362ae8d9343849ec39456). _GitHub_. [Archived](https://web.archive.org/web/20260526095500/https://github.com/google-research/bert/commit/fe354751d7de010f60d362ae8d9343849ec39456) from the original on May 26, 2026. Retrieved May 26, 2026.
  2. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:0_2-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:0_2-1) [_**c**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:0_2-2) [_**d**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:0_2-3) [_**e**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:0_2-4) [_**f**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:0_2-5) Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (October 11, 2018). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1810.04805v2](https://arxiv.org/abs/1810.04805v2) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  3. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-3)** ["Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing"](http://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html). _Google AI Blog_. November 2, 2018. Retrieved November 27, 2019.
  4. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:4_4-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:4_4-1) [_**c**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:4_4-2) Rogers, Anna; Kovaleva, Olga; Rumshisky, Anna (2020). ["A Primer in BERTology: What We Know About How BERT Works"](https://aclanthology.org/2020.tacl-1.54). _Transactions of the Association for Computational Linguistics_. **8** : 842–866. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2002.12327](https://arxiv.org/abs/2002.12327). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1162/tacl_a_00349](https://doi.org/10.1162%2Ftacl_a_00349). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [211532403](https://api.semanticscholar.org/CorpusID:211532403).
  5. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:5_5-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:5_5-1) Ethayarajh, Kawin (September 1, 2019), _How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1909.00512](https://arxiv.org/abs/1909.00512)
  6. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-6)** Anderson, Dawn (November 5, 2019). ["A deep dive into BERT: How BERT launched a rocket into natural language understanding"](https://searchengineland.com/a-deep-dive-into-bert-how-bert-launched-a-rocket-into-natural-language-understanding-324522). _Search Engine Land_. Retrieved August 6, 2024.
  7. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-bookcorpus_7-0)** Zhu, Yukun; Kiros, Ryan; Zemel, Rich; Salakhutdinov, Ruslan; Urtasun, Raquel; Torralba, Antonio; Fidler, Sanja (2015). "Aligning Books and Movies: Towards Story-Like Visual Explanations by Watching Movies and Reading Books". pp. 19–27. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1506.06724](https://arxiv.org/abs/1506.06724) [[cs.CV](https://arxiv.org/archive/cs.CV)].
  8. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:3_8-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:3_8-1) [_**c**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:3_8-2) ["BERT"](https://github.com/google-research/bert). _GitHub_. Retrieved March 28, 2023.
  9. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-9)** Zhang, Tianyi; Wu, Felix; Katiyar, Arzoo; Weinberger, Kilian Q.; Artzi, Yoav (March 11, 2021), _Revisiting Few-sample BERT Fine-tuning_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2006.05987](https://arxiv.org/abs/2006.05987)
  10. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-10)** Turc, Iulia; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (September 25, 2019), _Well-Read Students Learn Better: On the Importance of Pre-training Compact Models_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1908.08962](https://arxiv.org/abs/1908.08962)
  11. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-11)** ["Summary of the models — transformers 3.4.0 documentation"](https://huggingface.co/transformers/v3.4.0/model_summary.html). _huggingface.co_. Retrieved February 16, 2023.
  12. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-12)** Tay, Yi; Dehghani, Mostafa; Tran, Vinh Q.; Garcia, Xavier; Wei, Jason; Wang, Xuezhi; Chung, Hyung Won; Shakeri, Siamak; Bahri, Dara (February 28, 2023), _UL2: Unifying Language Learning Paradigms_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2205.05131](https://arxiv.org/abs/2205.05131)
  13. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-zhangetal2024_13-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-zhangetal2024_13-1) Zhang, Aston; Lipton, Zachary; Li, Mu; Smola, Alexander J. (2024). ["11.9. Large-Scale Pretraining with Transformers"](https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html). _Dive into deep learning_. Cambridge New York Port Melbourne New Delhi Singapore: Cambridge University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-009-38943-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-009-38943-3 "Special:BookSources/978-1-009-38943-3").
  14. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-14)** Rajpurkar, Pranav; Zhang, Jian; Lopyrev, Konstantin; [Liang, Percy](https://en.wikipedia.org/wiki/Percy_Liang "Percy Liang") (October 10, 2016). "SQuAD: 100,000+ Questions for Machine Comprehension of Text". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1606.05250](https://arxiv.org/abs/1606.05250) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  15. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-15)** Zellers, Rowan; Bisk, Yonatan; Schwartz, Roy; Choi, Yejin (August 15, 2018). "SWAG: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1808.05326](https://arxiv.org/abs/1808.05326) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  16. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-16)** ["bert/modeling.py at master · google-research/bert"](https://github.com/google-research/bert/blob/master/modeling.py). _GitHub_. Retrieved September 16, 2024.
  17. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:1_17-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:1_17-1) Kovaleva, Olga; Romanov, Alexey; Rogers, Anna; Rumshisky, Anna (November 2019). ["Revealing the Dark Secrets of BERT"](https://www.aclweb.org/anthology/D19-1445). _Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)_. pp. 4364–4373. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/D19-1445](https://doi.org/10.18653%2Fv1%2FD19-1445). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [201645145](https://api.semanticscholar.org/CorpusID:201645145).
  18. ^ [_**a**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:2_18-0) [_**b**_](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-:2_18-1) Clark, Kevin; Khandelwal, Urvashi; Levy, Omer; Manning, Christopher D. (2019). ["What Does BERT Look at? An Analysis of BERT's Attention"](https://doi.org/10.18653%2Fv1%2Fw19-4828). _Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP_. Stroudsburg, PA, USA: Association for Computational Linguistics: 276–286. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1906.04341](https://arxiv.org/abs/1906.04341). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/w19-4828](https://doi.org/10.18653%2Fv1%2Fw19-4828).
  19. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-19)** Khandelwal, Urvashi; He, He; Qi, Peng; Jurafsky, Dan (2018). "Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context". _Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_. Stroudsburg, PA, USA: Association for Computational Linguistics: 284–294. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1805.04623](https://arxiv.org/abs/1805.04623). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/p18-1027](https://doi.org/10.18653%2Fv1%2Fp18-1027). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [21700944](https://api.semanticscholar.org/CorpusID:21700944).
  20. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-20)** Gulordava, Kristina; Bojanowski, Piotr; Grave, Edouard; Linzen, Tal; Baroni, Marco (2018). "Colorless Green Recurrent Networks Dream Hierarchically". _Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)_. Stroudsburg, PA, USA: Association for Computational Linguistics. pp. 1195–1205. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1803.11138](https://arxiv.org/abs/1803.11138). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/n18-1108](https://doi.org/10.18653%2Fv1%2Fn18-1108). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [4460159](https://api.semanticscholar.org/CorpusID:4460159).
  21. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-21)** Giulianelli, Mario; Harding, Jack; Mohnert, Florian; Hupkes, Dieuwke; Zuidema, Willem (2018). "Under the Hood: Using Diagnostic Classifiers to Investigate and Improve how Language Models Track Agreement Information". _Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP_. Stroudsburg, PA, USA: Association for Computational Linguistics: 240–248. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1808.08079](https://arxiv.org/abs/1808.08079). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/w18-5426](https://doi.org/10.18653%2Fv1%2Fw18-5426). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [52090220](https://api.semanticscholar.org/CorpusID:52090220).
  22. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-22)** Zhang, Kelly; Bowman, Samuel (2018). ["Language Modeling Teaches You More than Translation Does: Lessons Learned Through Auxiliary Syntactic Task Analysis"](https://doi.org/10.18653%2Fv1%2Fw18-5448). _Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP_. Stroudsburg, PA, USA: Association for Computational Linguistics: 359–361. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/w18-5448](https://doi.org/10.18653%2Fv1%2Fw18-5448).
  23. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-23)** Sur, Chiranjib (January 2020). ["RBN: enhancement in language attribute prediction using global representation of natural language transfer learning technology like Google BERT"](https://doi.org/10.1007%2Fs42452-019-1765-9). _SN Applied Sciences_. **2** (1) 22. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/s42452-019-1765-9](https://doi.org/10.1007%2Fs42452-019-1765-9).
  24. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-24)** Patel, Ajay; Li, Bryan; Mohammad Sadegh Rasooli; Constant, Noah; Raffel, Colin; Callison-Burch, Chris (2022). "Bidirectional Language Models Are Also Few-shot Learners". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2209.14500](https://arxiv.org/abs/2209.14500) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  25. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-25)** Dai, Andrew; Le, Quoc (November 4, 2015). "Semi-supervised Sequence Learning". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1511.01432](https://arxiv.org/abs/1511.01432) [[cs.LG](https://arxiv.org/archive/cs.LG)].
  26. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-26)** Peters, Matthew; Neumann, Mark; Iyyer, Mohit; Gardner, Matt; Clark, Christopher; Lee, Kenton; Luke, Zettlemoyer (February 15, 2018). "Deep contextualized word representations". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1802.05365v2](https://arxiv.org/abs/1802.05365v2) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  27. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-27)** Howard, Jeremy; Ruder, Sebastian (January 18, 2018). "Universal Language Model Fine-tuning for Text Classification". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1801.06146v5](https://arxiv.org/abs/1801.06146v5) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  28. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-28)** Nayak, Pandu (October 25, 2019). ["Understanding searches better than ever before"](https://www.blog.google/products/search/search-language-understanding-bert/). _Google Blog_. Retrieved December 10, 2019.
  29. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-29)** ["Understanding searches better than ever before"](https://blog.google/products/search/search-language-understanding-bert/). _Google_. October 25, 2019. Retrieved August 6, 2024.
  30. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-30)** Montti, Roger (December 10, 2019). ["Google's BERT Rolls Out Worldwide"](https://www.searchenginejournal.com/google-bert-rolls-out-worldwide/339359/). _Search Engine Journal_. Retrieved December 10, 2019.
  31. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-31)** ["Google: BERT now used on almost every English query"](https://searchengineland.com/google-bert-used-on-almost-every-english-query-342193). _Search Engine Land_. October 15, 2020. Retrieved November 24, 2020.
  32. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-32)** Liu, Yinhan; Ott, Myle; Goyal, Naman; Du, Jingfei; Joshi, Mandar; Chen, Danqi; Levy, Omer; Lewis, Mike; Zettlemoyer, Luke; Stoyanov, Veselin (2019). "RoBERTa: A Robustly Optimized BERT Pretraining Approach". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1907.11692](https://arxiv.org/abs/1907.11692) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  33. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-33)** Conneau, Alexis; Khandelwal, Kartikay; Goyal, Naman; Chaudhary, Vishrav; Wenzek, Guillaume; Guzmán, Francisco; Grave, Edouard; Ott, Myle; Zettlemoyer, Luke; Stoyanov, Veselin (2019). "Unsupervised Cross-lingual Representation Learning at Scale". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1911.02116](https://arxiv.org/abs/1911.02116) [[cs.CL](https://arxiv.org/archive/cs.CL)].
  34. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-34)** Sanh, Victor; Debut, Lysandre; Chaumond, Julien; Wolf, Thomas (February 29, 2020), _DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1910.01108](https://arxiv.org/abs/1910.01108)
  35. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-35)** ["DistilBERT"](https://huggingface.co/docs/transformers/model_doc/distilbert). _huggingface.co_. Retrieved August 5, 2024.
  36. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-36)** Jiao, Xiaoqi; Yin, Yichun; Shang, Lifeng; Jiang, Xin; Chen, Xiao; Li, Linlin; Wang, Fang; Liu, Qun (October 15, 2020), _TinyBERT: Distilling BERT for Natural Language Understanding_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1909.10351](https://arxiv.org/abs/1909.10351)
  37. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-37)** Lan, Zhenzhong; Chen, Mingda; Goodman, Sebastian; Gimpel, Kevin; Sharma, Piyush; Soricut, Radu (February 8, 2020), _ALBERT: A Lite BERT for Self-supervised Learning of Language Representations_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1909.11942](https://arxiv.org/abs/1909.11942)
  38. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-38)** Clark, Kevin; Luong, Minh-Thang; Le, Quoc V.; Manning, Christopher D. (March 23, 2020), _ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2003.10555](https://arxiv.org/abs/2003.10555)
  39. **[^](https://en.wikipedia.org/wiki/BERT_\(language_model\)#cite_ref-39)** He, Pengcheng; Liu, Xiaodong; Gao, Jianfeng; Chen, Weizhu (October 6, 2021), _DeBERTa: Decoding-enhanced BERT with Disentangled Attention_ , [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2006.03654](https://arxiv.org/abs/2006.03654)


## Further reading
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=15 "Edit section: Further reading")]
  * Rogers, Anna; Kovaleva, Olga; Rumshisky, Anna (2020). "A Primer in BERTology: What we know about how BERT works". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2002.12327](https://arxiv.org/abs/2002.12327) [[cs.CL](https://arxiv.org/archive/cs.CL)].


## External links
[[edit](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&action=edit&section=16 "Edit section: External links")]
  * [Official GitHub repository](https://github.com/google-research/bert)

  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Google_AI "Template:Google AI")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Google_AI "Template talk:Google AI")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Google_AI "Special:EditPage/Template:Google AI")

[Google AI](https://en.wikipedia.org/wiki/Google_AI "Google AI")  |  
| --- |  
| 
  * [Google](https://en.wikipedia.org/wiki/Google "Google")
  * [Google Brain](https://en.wikipedia.org/wiki/Google_Brain "Google Brain")
  * [Google DeepMind](https://en.wikipedia.org/wiki/Google_DeepMind "Google DeepMind")

 |  
| Computer   
programs  |   
 | AlphaGo  |   
 | Versions  | 
  * [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo "AlphaGo") (2015)
  * [Master](https://en.wikipedia.org/wiki/Master_\(software\) "Master \(software\)") (2016)
  * [AlphaGo Zero](https://en.wikipedia.org/wiki/AlphaGo_Zero "AlphaGo Zero") (2017)
  * [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero "AlphaZero") (2017)
  * [MuZero](https://en.wikipedia.org/wiki/MuZero "MuZero") (2019)

 |  
| --- | --- |  
| Competitions  | 
  * [Fan Hui](https://en.wikipedia.org/wiki/AlphaGo_versus_Fan_Hui "AlphaGo versus Fan Hui") (2015)
  * [Lee Sedol](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol "AlphaGo versus Lee Sedol") (2016)
  * [Ke Jie](https://en.wikipedia.org/wiki/AlphaGo_versus_Ke_Jie "AlphaGo versus Ke Jie") (2017)

 |  
| In popular culture  | 
  * _[AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_\(film\) "AlphaGo \(film\)")_ (2017)

 |  
 |  
| Other  | 
  * [AlphaFold](https://en.wikipedia.org/wiki/AlphaFold "AlphaFold") (2018)
  * [AlphaStar](https://en.wikipedia.org/wiki/AlphaStar_\(software\) "AlphaStar \(software\)") (2019)
  * [AlphaTensor](https://en.wikipedia.org/wiki/AlphaTensor "AlphaTensor") (2022)
  * [AlphaDev](https://en.wikipedia.org/wiki/AlphaDev "AlphaDev") (2023)
  * [AlphaGeometry](https://en.wikipedia.org/wiki/AlphaGeometry "AlphaGeometry") (2024)
  * [AlphaGenome](https://en.wikipedia.org/wiki/AlphaGenome "AlphaGenome") (2025)

 |  
 |  
| Machine   
learning  |   
 | Neural networks  | 
  * [Inception](https://en.wikipedia.org/wiki/Inception_\(deep_learning_architecture\) "Inception \(deep learning architecture\)") (2014)
  * [WaveNet](https://en.wikipedia.org/wiki/WaveNet "WaveNet") (2016)
  * [MobileNet](https://en.wikipedia.org/wiki/MobileNet "MobileNet") (2017)
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\) "Transformer \(deep learning architecture\)") (2017)
  * [EfficientNet](https://en.wikipedia.org/wiki/EfficientNet "EfficientNet") (2019)
  * [Gato](https://en.wikipedia.org/wiki/Gato_\(DeepMind\) "Gato \(DeepMind\)") (2022)

 |  
| --- | --- |  
| Other  | 
  * [Quantum Artificial Intelligence Lab](https://en.wikipedia.org/wiki/Quantum_Artificial_Intelligence_Lab "Quantum Artificial Intelligence Lab")
  * [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow "TensorFlow")
  * [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_Processing_Unit "Tensor Processing Unit")

 |  
 |  
| Generative   
AI  |   
 | Chatbots  | 
  * [Assistant](https://en.wikipedia.org/wiki/Google_Assistant "Google Assistant") (2016)
  * [Sparrow](https://en.wikipedia.org/wiki/Sparrow_\(chatbot\) "Sparrow \(chatbot\)") (2022)
  * [Gemini](https://en.wikipedia.org/wiki/Google_Gemini "Google Gemini") (2023)
  * [Nano Banana](https://en.wikipedia.org/wiki/Nano_Banana "Nano Banana") (2025)

 |  
| --- | --- |  
| Models  | 
  * BERT (2018)
  * [XLNet](https://en.wikipedia.org/wiki/XLNet "XLNet") (2019)
  * [T5](https://en.wikipedia.org/wiki/T5_\(language_model\) "T5 \(language model\)") (2019)
  * [LaMDA](https://en.wikipedia.org/wiki/LaMDA "LaMDA") (2021)
  * [Chinchilla](https://en.wikipedia.org/wiki/Chinchilla_\(language_model\) "Chinchilla \(language model\)") (2022)
  * [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM") (2022)
  * [Imagen](https://en.wikipedia.org/wiki/Imagen_\(text-to-image_model\) "Imagen \(text-to-image model\)") (2023)
  * [Gemini](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini \(language model\)") (2023)
  * [VideoPoet](https://en.wikipedia.org/wiki/VideoPoet "VideoPoet") (2024)
  * [Gemma](https://en.wikipedia.org/wiki/Gemma_\(language_model\) "Gemma \(language model\)") (2024)
  * [Genie](https://en.wikipedia.org/wiki/Genie_\(AI_model\) "Genie \(AI model\)") (2024)
  * [Veo](https://en.wikipedia.org/wiki/Veo_\(text-to-video_model\) "Veo \(text-to-video model\)") (2024)

 |  
| Other  | 
  * [DreamBooth](https://en.wikipedia.org/wiki/DreamBooth "DreamBooth") (2022)
  * [NotebookLM](https://en.wikipedia.org/wiki/NotebookLM "NotebookLM") (2023)
  * [Vids](https://en.wikipedia.org/wiki/Google_Vids "Google Vids") (2024)
  * [Gemini Robotics](https://en.wikipedia.org/wiki/Gemini_Robotics "Gemini Robotics") (2025)
  * [Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity "Google Antigravity") (2025)

 |  
 |  
| See also  | 
  * "[Attention Is All You Need](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need "Attention Is All You Need")"
  * [Future of Go Summit](https://en.wikipedia.org/wiki/Future_of_Go_Summit "Future of Go Summit")
  * [Generative pre-trained transformer](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
  * [Google Labs](https://en.wikipedia.org/wiki/Google_Labs "Google Labs")
  * [Google Workspace](https://en.wikipedia.org/wiki/Google_Workspace "Google Workspace")

 |  
| 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category](https://en.wikipedia.org/wiki/Category:Google_DeepMind "Category:Google DeepMind")
  * [![](https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png)](https://en.wikipedia.org/wiki/File:Commons-logo.svg "Commons page") [Commons](https://commons.wikimedia.org/wiki/Category:DeepMind "commons:Category:DeepMind")

 |  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Google_LLC "Template:Google LLC")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Google_LLC "Template talk:Google LLC")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Google_LLC "Special:EditPage/Template:Google LLC")

[Google](https://en.wikipedia.org/wiki/Google "Google")  |  
| --- |  
| a subsidiary of [Alphabet](https://en.wikipedia.org/wiki/Alphabet_Inc. "Alphabet Inc.")  |  
|   
 | Company |  
| --- |  
|   
 | Divisions  | 
  * [AI](https://en.wikipedia.org/wiki/Google_AI "Google AI")
  * _[Area 120](https://en.wikipedia.org/wiki/Area_120 "Area 120")_
  * [ATAP](https://en.wikipedia.org/wiki/Google_ATAP "Google ATAP")
  * _[Brain](https://en.wikipedia.org/wiki/Google_Brain "Google Brain")_
  * [China](https://en.wikipedia.org/wiki/Google_China "Google China")
  * [Cloud Platform](https://en.wikipedia.org/wiki/Google_Cloud_Platform "Google Cloud Platform")
  * [Energy](https://en.wikipedia.org/wiki/Google_Energy "Google Energy")
  * [Google.org](https://en.wikipedia.org/wiki/Google.org "Google.org")
    * [Crisis Response](https://en.wikipedia.org/wiki/Google_Crisis_Response "Google Crisis Response")
  * [Registry](https://en.wikipedia.org/wiki/Google_Registry "Google Registry")

 |  
| --- | --- |  
| Subsidiaries  |   
 | Active  | 
  * [DeepMind](https://en.wikipedia.org/wiki/Google_DeepMind "Google DeepMind")
  * [Fitbit](https://en.wikipedia.org/wiki/Fitbit "Fitbit")
  * [ITA Software](https://en.wikipedia.org/wiki/ITA_Software "ITA Software")
  * [Jigsaw](https://en.wikipedia.org/wiki/Jigsaw_\(company\) "Jigsaw \(company\)")
  * [Looker](https://en.wikipedia.org/wiki/Looker_\(company\) "Looker \(company\)")
  * [Mandiant](https://en.wikipedia.org/wiki/Mandiant "Mandiant")
  * [Security Operations](https://en.wikipedia.org/wiki/Google_Security_Operations "Google Security Operations")
  * [Owlchemy Labs](https://en.wikipedia.org/wiki/Owlchemy_Labs "Owlchemy Labs")

 |  
| --- | --- |  
| Defunct  | 
  * [Actifio](https://en.wikipedia.org/wiki/Actifio "Actifio")
  * [Adscape](https://en.wikipedia.org/wiki/Adscape "Adscape")
  * [Akwan Information Technologies](https://en.wikipedia.org/wiki/Akwan_Information_Technologies "Akwan Information Technologies")
  * [Anvato](https://en.wikipedia.org/wiki/Anvato "Anvato")
  * [Apigee](https://en.wikipedia.org/wiki/Apigee "Apigee")
  * [BandPage](https://en.wikipedia.org/wiki/BandPage "BandPage")
  * [Bitium](https://en.wikipedia.org/wiki/Bitium "Bitium")
  * [BufferBox](https://en.wikipedia.org/wiki/BufferBox "BufferBox")
  * [Crashlytics](https://en.wikipedia.org/wiki/Crashlytics "Crashlytics")
  * [Dodgeball](https://en.wikipedia.org/wiki/Dodgeball_\(service\) "Dodgeball \(service\)")
  * [DoubleClick](https://en.wikipedia.org/wiki/DoubleClick "DoubleClick")
  * [Dropcam](https://en.wikipedia.org/wiki/Dropcam "Dropcam")
  * [Endoxon](https://en.wikipedia.org/wiki/Endoxon "Endoxon")
  * [Flutter](https://en.wikipedia.org/wiki/Flutter_\(American_company\) "Flutter \(American company\)")
  * [Global IP Solutions](https://en.wikipedia.org/wiki/Global_IP_Solutions "Global IP Solutions")
  * [Green Throttle Games](https://en.wikipedia.org/wiki/Green_Throttle_Games "Green Throttle Games")
  * [GreenBorder](https://en.wikipedia.org/wiki/GreenBorder "GreenBorder")
  * [Gridcentric](https://en.wikipedia.org/wiki/Gridcentric "Gridcentric")
  * [ImageAmerica](https://en.wikipedia.org/wiki/ImageAmerica "ImageAmerica")
  * [Impermium](https://en.wikipedia.org/wiki/Impermium "Impermium")
  * [Invite Media](https://en.wikipedia.org/wiki/Invite_Media "Invite Media")
  * [Kaltix](https://en.wikipedia.org/wiki/Kaltix "Kaltix")
  * [Marratech](https://en.wikipedia.org/wiki/Marratech "Marratech")
  * [Meebo](https://en.wikipedia.org/wiki/Meebo "Meebo")
  * [Metaweb](https://en.wikipedia.org/wiki/Metaweb "Metaweb")
  * [Neotonic Software](https://en.wikipedia.org/wiki/Neotonic_Software "Neotonic Software")
  * [Neverware](https://en.wikipedia.org/wiki/Neverware "Neverware")
  * [Nik Software](https://en.wikipedia.org/wiki/Nik_Software "Nik Software")
  * [Orbitera](https://en.wikipedia.org/wiki/Orbitera "Orbitera")
  * [Pyra Labs](https://en.wikipedia.org/wiki/Pyra_Labs "Pyra Labs")
  * [Quest Visual](https://en.wikipedia.org/wiki/Quest_Visual "Quest Visual")
  * [Reqwireless](https://en.wikipedia.org/wiki/Reqwireless "Reqwireless")
  * [RightsFlow](https://en.wikipedia.org/wiki/RightsFlow "RightsFlow")
  * [Sidewalk Labs](https://en.wikipedia.org/wiki/Sidewalk_Labs "Sidewalk Labs")
  * [SlickLogin](https://en.wikipedia.org/wiki/SlickLogin "SlickLogin")
  * [Titan Aerospace](https://en.wikipedia.org/wiki/Titan_Aerospace "Titan Aerospace")
  * [Typhoon Studios](https://en.wikipedia.org/wiki/Typhoon_Studios "Typhoon Studios")
  * [Urban Engines](https://en.wikipedia.org/wiki/Urban_Engines "Urban Engines")
  * [Vicarious](https://en.wikipedia.org/wiki/Vicarious_\(company\) "Vicarious \(company\)")
  * [Viewdle](https://en.wikipedia.org/wiki/Viewdle "Viewdle")
  * [Wavii](https://en.wikipedia.org/wiki/Wavii "Wavii")
  * [Wildfire Interactive](https://en.wikipedia.org/wiki/Wildfire_Interactive "Wildfire Interactive")
  * [YouTube Next Lab and Audience Development Group](https://en.wikipedia.org/wiki/YouTube_Next_Lab_and_Audience_Development_Group "YouTube Next Lab and Audience Development Group")

 |  
 |  
| Programs  | 
  * _[Business Groups](https://en.wikipedia.org/wiki/Google_Business_Groups "Google Business Groups")_
  * _[Computing University Initiative](https://en.wikipedia.org/wiki/IBM/Google_Cloud_Computing_University_Initiative "IBM/Google Cloud Computing University Initiative")_
  * _[Contact Lens](https://en.wikipedia.org/wiki/Google_Contact_Lens "Google Contact Lens")_
  * [Content ID](https://en.wikipedia.org/wiki/Content_ID "Content ID")
  * _[CrossCheck](https://en.wikipedia.org/wiki/CrossCheck_\(project\) "CrossCheck \(project\)")_
  * _[Data Liberation Front](https://en.wikipedia.org/wiki/Google_Data_Liberation_Front "Google Data Liberation Front")_
  * [Data Transfer Project](https://en.wikipedia.org/wiki/Data_Transfer_Project "Data Transfer Project")
  * [Developer Expert](https://en.wikipedia.org/wiki/Google_Developer_Expert "Google Developer Expert")
  * [DigiKavach](https://en.wikipedia.org/wiki/DigiKavach "DigiKavach")
  * _[DigiPivot](https://en.wikipedia.org/wiki/DigiPivot "DigiPivot")_
  * [Digital Garage](https://en.wikipedia.org/wiki/Google_Digital_Garage "Google Digital Garage")
  * [Digital News Initiative](https://en.wikipedia.org/wiki/Digital_News_Initiative "Digital News Initiative")
  * _[Digital Unlocked](https://en.wikipedia.org/wiki/Digital_Unlocked "Digital Unlocked")_
  * _[Dragonfly](https://en.wikipedia.org/wiki/Dragonfly_\(search_engine\) "Dragonfly \(search engine\)")_
  * _[Founders' Award](https://en.wikipedia.org/wiki/Google_Founders%27_Award "Google Founders' Award")_
  * _[Free Zone](https://en.wikipedia.org/wiki/Google_Free_Zone "Google Free Zone")_
  * [Get Your Business Online](https://en.wikipedia.org/wiki/Google_Get_Your_Business_Online "Google Get Your Business Online")
  * [Google for Education](https://en.wikipedia.org/wiki/Google_for_Education "Google for Education")
  * [Google for Health](https://en.wikipedia.org/wiki/Google_for_Health "Google for Health")
  * [Google for Startups](https://en.wikipedia.org/wiki/Google_for_Startups "Google for Startups")
  * _[Living Stories](https://en.wikipedia.org/wiki/Living_Stories "Living Stories")_
  * _[Made with Code](https://en.wikipedia.org/wiki/Made_with_Code "Made with Code")_
  * _[News Lab](https://en.wikipedia.org/wiki/Google_News_Lab "Google News Lab")_
  * _[PowerMeter](https://en.wikipedia.org/wiki/Google_PowerMeter "Google PowerMeter")_
  * [Privacy Sandbox](https://en.wikipedia.org/wiki/Privacy_Sandbox "Privacy Sandbox")
  * [Project Nightingale](https://en.wikipedia.org/wiki/Project_Nightingale "Project Nightingale")
  * [Project Nimbus](https://en.wikipedia.org/wiki/Project_Nimbus "Project Nimbus")
  * [Project Sunroof](https://en.wikipedia.org/wiki/Project_Sunroof "Project Sunroof")
  * [Project Zero](https://en.wikipedia.org/wiki/Project_Zero "Project Zero")
  * [Quantum Artificial Intelligence Lab](https://en.wikipedia.org/wiki/Quantum_Artificial_Intelligence_Lab "Quantum Artificial Intelligence Lab")
  * [RechargeIT](https://en.wikipedia.org/wiki/RechargeIT "RechargeIT")
  * [Sensorvault](https://en.wikipedia.org/wiki/Sensorvault "Sensorvault")
  * [Silicon Initiative](https://en.wikipedia.org/wiki/Google_Silicon_Initiative "Google Silicon Initiative")
  * _[Solve for X](https://en.wikipedia.org/wiki/Solve_for_X "Solve for X")_
  * [Street View Trusted](https://en.wikipedia.org/wiki/Street_View_Trusted "Street View Trusted")
  * _[Student Ambassador Program](https://en.wikipedia.org/wiki/Google_Student_Ambassador_Program "Google Student Ambassador Program")_
  * [Vevo](https://en.wikipedia.org/wiki/Vevo "Vevo")
  * [YouTube BrandConnect](https://en.wikipedia.org/wiki/YouTube_BrandConnect "YouTube BrandConnect")
  * [YouTube Creator Awards](https://en.wikipedia.org/wiki/YouTube_Creator_Awards "YouTube Creator Awards")
  * [YouTube Select](https://en.wikipedia.org/wiki/YouTube_Select "YouTube Select")
  * _[YouTube Original Channel Initiative](https://en.wikipedia.org/wiki/YouTube_Original_Channel_Initiative "YouTube Original Channel Initiative")_
  * [Year in Search](https://en.wikipedia.org/wiki/List_of_Year_in_Search_top_searches "List of Year in Search top searches")
  * _[YouTube Rewind](https://en.wikipedia.org/wiki/YouTube_Rewind "YouTube Rewind")_
    * [2018](https://en.wikipedia.org/wiki/YouTube_Rewind_2018:_Everyone_Controls_Rewind "YouTube Rewind 2018: Everyone Controls Rewind")
    * [2019](https://en.wikipedia.org/wiki/YouTube_Rewind_2019:_For_the_Record "YouTube Rewind 2019: For the Record")

 |  
| [Events](https://en.wikipedia.org/wiki/Category:Google_events "Category:Google events")  | 
  * [AlphaGo versus Fan Hui](https://en.wikipedia.org/wiki/AlphaGo_versus_Fan_Hui "AlphaGo versus Fan Hui")
  * [AlphaGo versus Lee Sedol](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol "AlphaGo versus Lee Sedol")
  * [AlphaGo versus Ke Jie](https://en.wikipedia.org/wiki/AlphaGo_versus_Ke_Jie "AlphaGo versus Ke Jie")
  * [Android Developer Challenge](https://en.wikipedia.org/wiki/Android_Developer_Challenge "Android Developer Challenge")
  * [Android Developer Day](https://en.wikipedia.org/wiki/Android_Developer_Day "Android Developer Day")
  * [Android Developer Lab](https://en.wikipedia.org/wiki/Android_Developer_Lab "Android Developer Lab")
  * [CNN/YouTube presidential debates](https://en.wikipedia.org/wiki/CNN/YouTube_presidential_debates "CNN/YouTube presidential debates")
  * [Code-in](https://en.wikipedia.org/wiki/Google_Code-in "Google Code-in")
  * [Code Jam](https://en.wikipedia.org/wiki/Google_Code_Jam "Google Code Jam")
  * [Developer Day](https://en.wikipedia.org/wiki/Google_Developer_Day "Google Developer Day")
  * [Developers Live](https://en.wikipedia.org/wiki/Google_Developers_Live "Google Developers Live")
  * [Doodle4Google](https://en.wikipedia.org/wiki/Doodle4Google "Doodle4Google")
  * [Future of Go Summit](https://en.wikipedia.org/wiki/Future_of_Go_Summit "Future of Go Summit")
  * [G-Day](https://en.wikipedia.org/wiki/G-Day "G-Day")
  * _[Hash Code](https://en.wikipedia.org/wiki/Hash_Code_\(programming_competition\) "Hash Code \(programming competition\)")_
  * [I/O](https://en.wikipedia.org/wiki/Google_I/O "Google I/O")
  * [Lunar X Prize](https://en.wikipedia.org/wiki/Google_Lunar_X_Prize "Google Lunar X Prize")
  * [Mapathon](https://en.wikipedia.org/wiki/Google_Mapathon "Google Mapathon")
  * [Science Fair](https://en.wikipedia.org/wiki/Google_Science_Fair "Google Science Fair")
  * [Summer of Code](https://en.wikipedia.org/wiki/Google_Summer_of_Code "Google Summer of Code")
  * [World Chess Championship 2024](https://en.wikipedia.org/wiki/World_Chess_Championship_2024 "World Chess Championship 2024")
  * [YouTube Awards](https://en.wikipedia.org/wiki/YouTube_Awards "YouTube Awards")
  * [YouTube Comedy Week](https://en.wikipedia.org/wiki/YouTube_Comedy_Week "YouTube Comedy Week")
  * [YouTube Live](https://en.wikipedia.org/wiki/YouTube_Live "YouTube Live")
  * [YouTube Music Awards](https://en.wikipedia.org/wiki/YouTube_Music_Awards "YouTube Music Awards")
    * [2013](https://en.wikipedia.org/wiki/2013_YouTube_Music_Awards "2013 YouTube Music Awards")
    * [2015](https://en.wikipedia.org/wiki/2015_YouTube_Music_Awards "2015 YouTube Music Awards")
  * [YouTube Space Lab](https://en.wikipedia.org/wiki/YouTube_Space_Lab "YouTube Space Lab")
  * [YouTube Symphony Orchestra](https://en.wikipedia.org/wiki/YouTube_Symphony_Orchestra "YouTube Symphony Orchestra")

 |  
| [Infrastructure](https://en.wikipedia.org/wiki/Category:Google_buildings_and_structures "Category:Google buildings and structures")  | 
  * [111 Eighth Avenue](https://en.wikipedia.org/wiki/111_Eighth_Avenue "111 Eighth Avenue")
  * [Android lawn statues](https://en.wikipedia.org/wiki/Android_lawn_statues "Android lawn statues")
  * _[Androidland](https://en.wikipedia.org/wiki/Androidland "Androidland")_
  * _[Barges](https://en.wikipedia.org/wiki/Google_barges "Google barges")_
  * [Binoculars Building](https://en.wikipedia.org/wiki/Binoculars_Building "Binoculars Building")
  * [Central Saint Giles](https://en.wikipedia.org/wiki/Central_Saint_Giles "Central Saint Giles")
  * [Chelsea Market](https://en.wikipedia.org/wiki/Chelsea_Market "Chelsea Market")
  * _[Chrome Zone](https://en.wikipedia.org/wiki/Chrome_Zone "Chrome Zone")_
  * [Data centers](https://en.wikipedia.org/wiki/Google_data_centers "Google data centers")
  * [GeoEye-1](https://en.wikipedia.org/wiki/GeoEye-1 "GeoEye-1")
  * [Googleplex](https://en.wikipedia.org/wiki/Googleplex "Googleplex")
  * [Ivanpah Solar Power Facility](https://en.wikipedia.org/wiki/Ivanpah_Solar_Power_Facility "Ivanpah Solar Power Facility")
  * [James R. Thompson Center](https://en.wikipedia.org/wiki/James_R._Thompson_Center "James R. Thompson Center")
  * [King's Cross](https://en.wikipedia.org/wiki/Google_King%27s_Cross "Google King's Cross")
  * [Mayfield Mall](https://en.wikipedia.org/wiki/Mayfield_Mall "Mayfield Mall")
  * [Pier 57](https://en.wikipedia.org/wiki/Pier_57 "Pier 57")
  * [Sidewalk Toronto](https://en.wikipedia.org/wiki/Sidewalk_Toronto "Sidewalk Toronto")
  * [St. John's Terminal](https://en.wikipedia.org/wiki/St._John%27s_Terminal "St. John's Terminal")
  * Submarine cables 
    * [Dunant](https://en.wikipedia.org/wiki/Dunant_\(submarine_communications_cable\) "Dunant \(submarine communications cable\)")
    * [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper_\(submarine_communications_cable\) "Grace Hopper \(submarine communications cable\)")
    * [Unity](https://en.wikipedia.org/wiki/Unity_\(cable_system\) "Unity \(cable system\)")
  * [WiFi](https://en.wikipedia.org/wiki/Google_WiFi "Google WiFi")
  * [YouTube Space](https://en.wikipedia.org/wiki/YouTube_Space "YouTube Space")
  * [YouTube Theater](https://en.wikipedia.org/wiki/YouTube_Theater "YouTube Theater")

 |  
| [People](https://en.wikipedia.org/wiki/Category:Google_employees "Category:Google employees")  |   
 | Current  | 
  * [Krishna Bharat](https://en.wikipedia.org/wiki/Krishna_Bharat "Krishna Bharat")
  * [Vint Cerf](https://en.wikipedia.org/wiki/Vint_Cerf "Vint Cerf")
  * [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean "Jeff Dean")
  * [John Doerr](https://en.wikipedia.org/wiki/John_Doerr "John Doerr")
  * [Sanjay Ghemawat](https://en.wikipedia.org/wiki/Sanjay_Ghemawat "Sanjay Ghemawat")
  * [Al Gore](https://en.wikipedia.org/wiki/Al_Gore "Al Gore")
  * [John L. Hennessy](https://en.wikipedia.org/wiki/John_L._Hennessy "John L. Hennessy")
  * [Urs Hölzle](https://en.wikipedia.org/wiki/Urs_H%C3%B6lzle "Urs Hölzle")
  * [Salar Kamangar](https://en.wikipedia.org/wiki/Salar_Kamangar "Salar Kamangar")
  * [Ray Kurzweil](https://en.wikipedia.org/wiki/Ray_Kurzweil "Ray Kurzweil")
  * [Ann Mather](https://en.wikipedia.org/wiki/Ann_Mather "Ann Mather")
  * [Alan Mulally](https://en.wikipedia.org/wiki/Alan_Mulally "Alan Mulally")
  * [Rick Osterloh](https://en.wikipedia.org/wiki/Rick_Osterloh "Rick Osterloh")
  * [Sundar Pichai](https://en.wikipedia.org/wiki/Sundar_Pichai "Sundar Pichai") (CEO)
  * [Ruth Porat](https://en.wikipedia.org/wiki/Ruth_Porat "Ruth Porat") (CFO)
  * [Rajen Sheth](https://en.wikipedia.org/wiki/Rajen_Sheth "Rajen Sheth")
  * [Hal Varian](https://en.wikipedia.org/wiki/Hal_Varian "Hal Varian")
  * [Neal Mohan](https://en.wikipedia.org/wiki/Neal_Mohan "Neal Mohan")

 |  
| --- | --- |  
| Former  | 
  * [Andy Bechtolsheim](https://en.wikipedia.org/wiki/Andy_Bechtolsheim "Andy Bechtolsheim")
  * [Sergey Brin](https://en.wikipedia.org/wiki/Sergey_Brin "Sergey Brin") (co-founder)
  * [David Cheriton](https://en.wikipedia.org/wiki/David_Cheriton "David Cheriton")
  * [Matt Cutts](https://en.wikipedia.org/wiki/Matt_Cutts "Matt Cutts")
  * [David Drummond](https://en.wikipedia.org/wiki/David_Drummond_\(businessman\) "David Drummond \(businessman\)")
  * [Alan Eustace](https://en.wikipedia.org/wiki/Alan_Eustace "Alan Eustace")
  * [Timnit Gebru](https://en.wikipedia.org/wiki/Timnit_Gebru "Timnit Gebru")
  * [Omid Kordestani](https://en.wikipedia.org/wiki/Omid_Kordestani "Omid Kordestani")
  * [Paul Otellini](https://en.wikipedia.org/wiki/Paul_Otellini "Paul Otellini")
  * [Larry Page](https://en.wikipedia.org/wiki/Larry_Page "Larry Page") (co-founder)
  * [Patrick Pichette](https://en.wikipedia.org/wiki/Patrick_Pichette "Patrick Pichette")
  * [Eric Schmidt](https://en.wikipedia.org/wiki/Eric_Schmidt "Eric Schmidt")
  * [Ram Shriram](https://en.wikipedia.org/wiki/Ram_Shriram "Ram Shriram")
  * [Amit Singhal](https://en.wikipedia.org/wiki/Amit_Singhal "Amit Singhal")
  * [Shirley M. Tilghman](https://en.wikipedia.org/wiki/Shirley_M._Tilghman "Shirley M. Tilghman")
  * [Rachel Whetstone](https://en.wikipedia.org/wiki/Rachel_Whetstone "Rachel Whetstone")
  * [Susan Wojcicki](https://en.wikipedia.org/wiki/Susan_Wojcicki "Susan Wojcicki")

 |  
 |  
| [Criticism](https://en.wikipedia.org/wiki/Criticism_of_Google "Criticism of Google")  |   
 | General  | 
  * [Censorship](https://en.wikipedia.org/wiki/Censorship_by_Google "Censorship by Google")
  * [DeGoogle](https://en.wikipedia.org/wiki/DeGoogle "DeGoogle")
  * [FairSearch](https://en.wikipedia.org/wiki/FairSearch "FairSearch")
  * "[Google's Ideological Echo Chamber](https://en.wikipedia.org/wiki/Google%27s_Ideological_Echo_Chamber "Google's Ideological Echo Chamber")"
  * [No Tech for Apartheid](https://en.wikipedia.org/wiki/No_Tech_for_Apartheid "No Tech for Apartheid")
  * [Privacy concerns](https://en.wikipedia.org/wiki/Privacy_concerns_with_Google "Privacy concerns with Google")
    * [Street View](https://en.wikipedia.org/wiki/Google_Street_View_privacy_concerns "Google Street View privacy concerns")
    * [YouTube](https://en.wikipedia.org/wiki/YouTube_and_privacy "YouTube and privacy")
  * [Trade unions](https://en.wikipedia.org/wiki/Google_and_trade_unions "Google and trade unions")
    * [Alphabet Workers Union](https://en.wikipedia.org/wiki/Alphabet_Workers_Union "Alphabet Workers Union")
  * [YouTube copyright issues](https://en.wikipedia.org/wiki/YouTube_copyright_issues "YouTube copyright issues")

 |  
| --- | --- |  
| Incidents  | 
  * [Backdoor advertisement controversy](https://en.wikipedia.org/wiki/2020_Korean_YouTube_backdoor_advertising_controversy "2020 Korean YouTube backdoor advertising controversy")
  * [Blocking of YouTube videos in Germany](https://en.wikipedia.org/wiki/Blocking_of_YouTube_videos_in_Germany "Blocking of YouTube videos in Germany")
  * [Data breach](https://en.wikipedia.org/wiki/2018_Google_data_breach "2018 Google data breach")
  * [Elsagate](https://en.wikipedia.org/wiki/Elsagate "Elsagate")
  * [Fantastic Adventures scandal](https://en.wikipedia.org/wiki/Fantastic_Adventures_scandal "Fantastic Adventures scandal")
  * [Kohistan video case](https://en.wikipedia.org/wiki/2012_Kohistan_video_case "2012 Kohistan video case")
  * [Reactions to _Innocence of Muslims_](https://en.wikipedia.org/wiki/Reactions_to_Innocence_of_Muslims "Reactions to Innocence of Muslims")
  * [San Francisco tech bus protests](https://en.wikipedia.org/wiki/San_Francisco_tech_bus_protests "San Francisco tech bus protests")
  * [Services outages](https://en.wikipedia.org/wiki/Google_services_outages "Google services outages")
  * [Slovenian government incident](https://en.wikipedia.org/wiki/2011_Slovenian_YouTube_incident "2011 Slovenian YouTube incident")
  * [Walkouts](https://en.wikipedia.org/wiki/2018_Google_walkouts "2018 Google walkouts")
  * [YouTube headquarters shooting](https://en.wikipedia.org/wiki/YouTube_headquarters_shooting "YouTube headquarters shooting")

 |  
 |  
| Other  | 
  * [Android apps](https://en.wikipedia.org/wiki/List_of_Android_apps_by_Google "List of Android apps by Google")
  * [April Fools' Day jokes](https://en.wikipedia.org/wiki/List_of_Google_April_Fools%27_Day_jokes "List of Google April Fools' Day jokes")
  * [Doodles](https://en.wikipedia.org/wiki/Google_Doodle "Google Doodle")
    * _[Doodle Champion Island Games](https://en.wikipedia.org/wiki/Doodle_Champion_Island_Games "Doodle Champion Island Games")_
    * _[Magic Cat Academy](https://en.wikipedia.org/wiki/Magic_Cat_Academy "Magic Cat Academy")_
    * _[Pac-Man](https://en.wikipedia.org/wiki/Pac-Man_Google_Doodle "Pac-Man Google Doodle")_
  * [Easter eggs](https://en.wikipedia.org/wiki/List_of_Google_Easter_eggs "List of Google Easter eggs")
  * [History](https://en.wikipedia.org/wiki/History_of_Google "History of Google")
    * [Gmail](https://en.wikipedia.org/wiki/History_of_Gmail "History of Gmail")
    * [Search](https://en.wikipedia.org/wiki/Timeline_of_Google_Search "Timeline of Google Search")
    * [YouTube](https://en.wikipedia.org/wiki/History_of_YouTube "History of YouTube")
  * [Logo](https://en.wikipedia.org/wiki/Google_logo "Google logo")
  * [Material Design](https://en.wikipedia.org/wiki/Material_Design "Material Design")
  * [Mergers and acquisitions](https://en.wikipedia.org/wiki/List_of_mergers_and_acquisitions_by_Alphabet "List of mergers and acquisitions by Alphabet")

 |  
 |  
 |  
|   
 | [Development](https://en.wikipedia.org/wiki/Google_Developers "Google Developers") |  
| --- |  
|   
 | Software  |   
 | A–C  | 
  * [Accelerated Linear Algebra](https://en.wikipedia.org/wiki/Accelerated_Linear_Algebra "Accelerated Linear Algebra")
  * [AMP](https://en.wikipedia.org/wiki/Accelerated_Mobile_Pages "Accelerated Mobile Pages")
  * _[Actions on Google](https://en.wikipedia.org/wiki/Actions_on_Google "Actions on Google")_
  * [ALTS](https://en.wikipedia.org/wiki/ALTS "ALTS")
  * [American Fuzzy Lop](https://en.wikipedia.org/wiki/American_Fuzzy_Lop_\(software\) "American Fuzzy Lop \(software\)")
  * _[Android Cloud to Device Messaging](https://en.wikipedia.org/wiki/Android_Cloud_to_Device_Messaging "Android Cloud to Device Messaging")_
  * [Android Debug Bridge](https://en.wikipedia.org/wiki/Android_Debug_Bridge "Android Debug Bridge")
  * [Android NDK](https://en.wikipedia.org/wiki/Android_NDK "Android NDK")
  * [Android Runtime](https://en.wikipedia.org/wiki/Android_Runtime "Android Runtime")
  * [Android SDK](https://en.wikipedia.org/wiki/Android_SDK "Android SDK")
  * [Android Studio](https://en.wikipedia.org/wiki/Android_Studio "Android Studio")
  * [Angular](https://en.wikipedia.org/wiki/Angular_\(web_framework\) "Angular \(web framework\)")
  * _[AngularJS](https://en.wikipedia.org/wiki/AngularJS "AngularJS")_
  * [Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity "Google Antigravity")
  * [Apache Beam](https://en.wikipedia.org/wiki/Apache_Beam "Apache Beam")
  * [APIs](https://en.wikipedia.org/wiki/Google_APIs "Google APIs")
  * [App Engine](https://en.wikipedia.org/wiki/Google_App_Engine "Google App Engine")
  * [App Inventor](https://en.wikipedia.org/wiki/MIT_App_Inventor "MIT App Inventor")
  * _[App Maker](https://en.wikipedia.org/wiki/Google_App_Maker "Google App Maker")_
  * [App Runtime for Chrome](https://en.wikipedia.org/wiki/Google_App_Runtime_for_Chrome "Google App Runtime for Chrome")
  * _[AppJet](https://en.wikipedia.org/wiki/AppJet "AppJet")_
  * [Apps Script](https://en.wikipedia.org/wiki/Google_Apps_Script "Google Apps Script")
  * [AppSheet](https://en.wikipedia.org/wiki/AppSheet "AppSheet")
  * [ARCore](https://en.wikipedia.org/wiki/ARCore "ARCore")
  * _[Base](https://en.wikipedia.org/wiki/Google_Base "Google Base")_
  * [Bazel](https://en.wikipedia.org/wiki/Bazel_\(software\) "Bazel \(software\)")
  * [BeyondCorp](https://en.wikipedia.org/wiki/BeyondCorp "BeyondCorp")
  * [Bigtable](https://en.wikipedia.org/wiki/Bigtable "Bigtable")
  * [BigQuery](https://en.wikipedia.org/wiki/BigQuery "BigQuery")
  * [Bionic](https://en.wikipedia.org/wiki/Bionic_\(software\) "Bionic \(software\)")
  * [Blockly](https://en.wikipedia.org/wiki/Blockly "Blockly")
  * _[Borg](https://en.wikipedia.org/wiki/Borg_\(cluster_manager\) "Borg \(cluster manager\)")_
  * _[Caja](https://en.wikipedia.org/wiki/Caja_project "Caja project")_
  * [Cameyo](https://en.wikipedia.org/wiki/Cameyo "Cameyo")
  * [Chart API](https://en.wikipedia.org/wiki/Google_Chart_API "Google Chart API")
  * [Charts](https://en.wikipedia.org/wiki/Google_Charts "Google Charts")
  * _[Chrome Frame](https://en.wikipedia.org/wiki/Google_Chrome_Frame "Google Chrome Frame")_
  * [Chromium](https://en.wikipedia.org/wiki/Chromium_\(web_browser\) "Chromium \(web browser\)")
    * [Blink](https://en.wikipedia.org/wiki/Blink_\(browser_engine\) "Blink \(browser engine\)")
  * [Closure Tools](https://en.wikipedia.org/wiki/Google_Closure_Tools "Google Closure Tools")
  * _[Cloud Connect](https://en.wikipedia.org/wiki/Google_Cloud_Connect "Google Cloud Connect")_
  * [Cloud Dataflow](https://en.wikipedia.org/wiki/Google_Cloud_Dataflow "Google Cloud Dataflow")
  * [Cloud Datastore](https://en.wikipedia.org/wiki/Google_Cloud_Datastore "Google Cloud Datastore")
  * _[Cloud Messaging](https://en.wikipedia.org/wiki/Google_Cloud_Messaging "Google Cloud Messaging")_
  * [Cloud Shell](https://en.wikipedia.org/wiki/Google_Cloud_Shell "Google Cloud Shell")
  * [Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage "Google Cloud Storage")
  * _[Code Search](https://en.wikipedia.org/wiki/Google_Code_Search "Google Code Search")_
  * [Compute Engine](https://en.wikipedia.org/wiki/Google_Compute_Engine "Google Compute Engine")
  * [Cpplint](https://en.wikipedia.org/wiki/Cpplint "Cpplint")

 |  
| --- | --- |  
| D–N  | 
  * _[Dalvik](https://en.wikipedia.org/wiki/Dalvik_\(software\) "Dalvik \(software\)")_
  * [Data Protocol](https://en.wikipedia.org/wiki/Google_Data_Protocol "Google Data Protocol")
  * [Data Studio](https://en.wikipedia.org/wiki/Data_Studio "Data Studio")
  * [Dialogflow](https://en.wikipedia.org/wiki/Dialogflow "Dialogflow")
  * [Exposure Notification](https://en.wikipedia.org/wiki/Exposure_Notification "Exposure Notification")
  * [Fast Pair](https://en.wikipedia.org/wiki/Fast_Pair "Fast Pair")
  * [Fastboot](https://en.wikipedia.org/wiki/Fastboot "Fastboot")
  * [Federated Learning of Cohorts](https://en.wikipedia.org/wiki/Federated_Learning_of_Cohorts "Federated Learning of Cohorts")
  * [File System](https://en.wikipedia.org/wiki/Google_File_System "Google File System")
  * [Firebase](https://en.wikipedia.org/wiki/Firebase "Firebase")
  * [Firebase Studio](https://en.wikipedia.org/wiki/Firebase_Studio "Firebase Studio")
  * [Firebase Cloud Messaging](https://en.wikipedia.org/wiki/Firebase_Cloud_Messaging "Firebase Cloud Messaging")
  * [FlatBuffers](https://en.wikipedia.org/wiki/FlatBuffers "FlatBuffers")
  * [Flutter](https://en.wikipedia.org/wiki/Flutter_\(software\) "Flutter \(software\)")
  * _[Freebase](https://en.wikipedia.org/wiki/Freebase_\(database\) "Freebase \(database\)")_
  * [Gadgets](https://en.wikipedia.org/wiki/Google_Gadgets "Google Gadgets")
  * [Ganeti](https://en.wikipedia.org/wiki/Ganeti "Ganeti")
  * _[Gears](https://en.wikipedia.org/wiki/Gears_\(software\) "Gears \(software\)")_
  * [Gerrit](https://en.wikipedia.org/wiki/Gerrit_\(software\) "Gerrit \(software\)")
  * [Global Cache](https://en.wikipedia.org/wiki/Google_Global_Cache "Google Global Cache")
  * [GLOP](https://en.wikipedia.org/wiki/GLOP "GLOP")
  * [gRPC](https://en.wikipedia.org/wiki/GRPC "GRPC")
  * [Gson](https://en.wikipedia.org/wiki/Gson "Gson")
  * [Guava](https://en.wikipedia.org/wiki/Google_Guava "Google Guava")
  * [Guetzli](https://en.wikipedia.org/wiki/Guetzli "Guetzli")
  * [Guice](https://en.wikipedia.org/wiki/Google_Guice "Google Guice")
  * [gVisor](https://en.wikipedia.org/wiki/GVisor "GVisor")
  * [GYP](https://en.wikipedia.org/wiki/GYP_\(software\) "GYP \(software\)")
  * [JAX](https://en.wikipedia.org/wiki/JAX_\(software\) "JAX \(software\)")
  * [Jetpack Compose](https://en.wikipedia.org/wiki/Jetpack_Compose "Jetpack Compose")
  * [Keyhole Markup Language](https://en.wikipedia.org/wiki/Keyhole_Markup_Language "Keyhole Markup Language")
  * [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes "Kubernetes")
  * [Kythe](https://en.wikipedia.org/wiki/Google_Kythe "Google Kythe")
  * [LevelDB](https://en.wikipedia.org/wiki/LevelDB "LevelDB")
  * [Lighthouse](https://en.wikipedia.org/wiki/Lighthouse_\(software\) "Lighthouse \(software\)")
  * _[lmctfy](https://en.wikipedia.org/wiki/Lmctfy "Lmctfy")_
  * [MapReduce](https://en.wikipedia.org/wiki/MapReduce "MapReduce")
  * _[Mashup Editor](https://en.wikipedia.org/wiki/Google_Mashup_Editor "Google Mashup Editor")_
  * [Matter](https://en.wikipedia.org/wiki/Matter_\(standard\) "Matter \(standard\)")
  * [Mobile Services](https://en.wikipedia.org/wiki/Google_Mobile_Services "Google Mobile Services")
  * [Namebench](https://en.wikipedia.org/wiki/Namebench "Namebench")
  * [Native Client](https://en.wikipedia.org/wiki/Google_Native_Client "Google Native Client")
  * [Neatx](https://en.wikipedia.org/wiki/Neatx "Neatx")
  * [Neural Machine Translation](https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation "Google Neural Machine Translation")
  * [Nomulus](https://en.wikipedia.org/wiki/Nomulus "Nomulus")

 |  
| O–Z  | 
  * [Open Location Code](https://en.wikipedia.org/wiki/Open_Location_Code "Open Location Code")
  * [OpenRefine](https://en.wikipedia.org/wiki/OpenRefine "OpenRefine")
  * [OpenSocial](https://en.wikipedia.org/wiki/OpenSocial "OpenSocial")
  * _[Optimize](https://en.wikipedia.org/wiki/Google_Optimize "Google Optimize")_
  * [OR-Tools](https://en.wikipedia.org/wiki/OR-Tools "OR-Tools")
  * _[Pack](https://en.wikipedia.org/wiki/Google_Pack "Google Pack")_
  * [PageSpeed](https://en.wikipedia.org/wiki/Google_PageSpeed_Tools "Google PageSpeed Tools")
  * [Piper](https://en.wikipedia.org/wiki/Piper_\(source_control_system\) "Piper \(source control system\)")
  * _[Plugin for Eclipse](https://en.wikipedia.org/wiki/Google_Plugin_for_Eclipse "Google Plugin for Eclipse")_
  * [Polymer](https://en.wikipedia.org/wiki/Polymer_\(library\) "Polymer \(library\)")
  * [Programmable Search Engine](https://en.wikipedia.org/wiki/Google_Programmable_Search_Engine "Google Programmable Search Engine")
  * [Project Shield](https://en.wikipedia.org/wiki/Project_Shield "Project Shield")
  * [Public DNS](https://en.wikipedia.org/wiki/Google_Public_DNS "Google Public DNS")
  * [reCAPTCHA](https://en.wikipedia.org/wiki/ReCAPTCHA "ReCAPTCHA")
  * _[RenderScript](https://en.wikipedia.org/wiki/RenderScript "RenderScript")_
  * [SafetyNet](https://en.wikipedia.org/wiki/SafetyNet "SafetyNet")
  * _[SageTV](https://en.wikipedia.org/wiki/SageTV "SageTV")_
  * [Schema.org](https://en.wikipedia.org/wiki/Schema.org "Schema.org")
  * [Search Console](https://en.wikipedia.org/wiki/Google_Search_Console "Google Search Console")
  * [Shell](https://en.wikipedia.org/wiki/Google_Shell "Google Shell")
  * [Sitemaps](https://en.wikipedia.org/wiki/Sitemaps "Sitemaps")
  * [Skia Graphics Engine](https://en.wikipedia.org/wiki/Skia_Graphics_Engine "Skia Graphics Engine")
  * [Spanner](https://en.wikipedia.org/wiki/Spanner_\(database\) "Spanner \(database\)")
  * _[Sputnik](https://en.wikipedia.org/wiki/Sputnik_\(JavaScript_conformance_test\) "Sputnik \(JavaScript conformance test\)")_
  * _[Stackdriver](https://en.wikipedia.org/wiki/Stackdriver "Stackdriver")_
  * _[Swiffy](https://en.wikipedia.org/wiki/Google_Swiffy "Google Swiffy")_
  * _[Tango](https://en.wikipedia.org/wiki/Tango_\(platform\) "Tango \(platform\)")_
  * [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow "TensorFlow")
  * [Tesseract](https://en.wikipedia.org/wiki/Tesseract_\(software\) "Tesseract \(software\)")
  * [Test](https://en.wikipedia.org/wiki/Google_Test "Google Test")
  * _[Translator Toolkit](https://en.wikipedia.org/wiki/Google_Translator_Toolkit "Google Translator Toolkit")_
  * _[Urchin](https://en.wikipedia.org/wiki/Urchin_\(software\) "Urchin \(software\)")_
    * [UTM parameters](https://en.wikipedia.org/wiki/UTM_parameters "UTM parameters")
  * [V8](https://en.wikipedia.org/wiki/V8_\(JavaScript_engine\) "V8 \(JavaScript engine\)")
  * [VirusTotal](https://en.wikipedia.org/wiki/VirusTotal "VirusTotal")
  * [VisBug](https://en.wikipedia.org/wiki/VisBug "VisBug")
  * [Wave Federation Protocol](https://en.wikipedia.org/wiki/Google_Wave_Federation_Protocol "Google Wave Federation Protocol")
  * [Weave](https://en.wikipedia.org/wiki/Weave_\(protocol\) "Weave \(protocol\)")
  * _[Web Accelerator](https://en.wikipedia.org/wiki/Google_Web_Accelerator "Google Web Accelerator")_
  * [Web Designer](https://en.wikipedia.org/wiki/Google_Web_Designer "Google Web Designer")
  * [Web Server](https://en.wikipedia.org/wiki/Google_Web_Server "Google Web Server")
  * [Web Toolkit](https://en.wikipedia.org/wiki/Google_Web_Toolkit "Google Web Toolkit")
  * [Webdriver Torso](https://en.wikipedia.org/wiki/Webdriver_Torso "Webdriver Torso")
  * [WebRTC](https://en.wikipedia.org/wiki/WebRTC "WebRTC")

 |  
 |  
| Operating systems  | 
  * [Android](https://en.wikipedia.org/wiki/Android_\(operating_system\) "Android \(operating system\)")
    * [Cupcake](https://en.wikipedia.org/wiki/Android_Cupcake "Android Cupcake")
    * [Donut](https://en.wikipedia.org/wiki/Android_Donut "Android Donut")
    * [Eclair](https://en.wikipedia.org/wiki/Android_Eclair "Android Eclair")
    * [Froyo](https://en.wikipedia.org/wiki/Android_Froyo "Android Froyo")
    * [Gingerbread](https://en.wikipedia.org/wiki/Android_Gingerbread "Android Gingerbread")
    * [Honeycomb](https://en.wikipedia.org/wiki/Android_Honeycomb "Android Honeycomb")
    * [Ice Cream Sandwich](https://en.wikipedia.org/wiki/Android_Ice_Cream_Sandwich "Android Ice Cream Sandwich")
    * [Jelly Bean](https://en.wikipedia.org/wiki/Android_Jelly_Bean "Android Jelly Bean")
    * [KitKat](https://en.wikipedia.org/wiki/Android_KitKat "Android KitKat")
    * [Lollipop](https://en.wikipedia.org/wiki/Android_Lollipop "Android Lollipop")
    * [Marshmallow](https://en.wikipedia.org/wiki/Android_Marshmallow "Android Marshmallow")
    * [Nougat](https://en.wikipedia.org/wiki/Android_Nougat "Android Nougat")
    * [Oreo](https://en.wikipedia.org/wiki/Android_Oreo "Android Oreo")
    * [Pie](https://en.wikipedia.org/wiki/Android_Pie "Android Pie")
    * [10](https://en.wikipedia.org/wiki/Android_10 "Android 10")
    * [11](https://en.wikipedia.org/wiki/Android_11 "Android 11")
    * [12](https://en.wikipedia.org/wiki/Android_12 "Android 12")
    * [13](https://en.wikipedia.org/wiki/Android_13 "Android 13")
    * [14](https://en.wikipedia.org/wiki/Android_14 "Android 14")
    * [15](https://en.wikipedia.org/wiki/Android_15 "Android 15")
    * [16](https://en.wikipedia.org/wiki/Android_16 "Android 16")
    * [version history](https://en.wikipedia.org/wiki/Android_version_history "Android version history")
    * [smartphones](https://en.wikipedia.org/wiki/List_of_Android_smartphones "List of Android smartphones")
  * [Android Automotive](https://en.wikipedia.org/wiki/Android_Automotive "Android Automotive")
  * [Android Go](https://en.wikipedia.org/wiki/Android_Go "Android Go")
    * [devices](https://en.wikipedia.org/wiki/Comparison_of_Android_Go_products "Comparison of Android Go products")
  * _[Android Things](https://en.wikipedia.org/wiki/Android_Things "Android Things")_
  * [Android TV](https://en.wikipedia.org/wiki/Android_TV "Android TV")
    * [Google TV interface](https://en.wikipedia.org/wiki/Google_TV_\(interface\) "Google TV \(interface\)")
    * [devices](https://en.wikipedia.org/wiki/List_of_Android_TV_devices "List of Android TV devices")
  * [Android XR](https://en.wikipedia.org/wiki/Android_XR "Android XR")
  * [ChromeOS](https://en.wikipedia.org/wiki/ChromeOS "ChromeOS")
  * [ChromeOS Flex](https://en.wikipedia.org/wiki/ChromeOS_Flex "ChromeOS Flex")
  * [ChromiumOS](https://en.wikipedia.org/wiki/ChromiumOS "ChromiumOS")
  * [Fuchsia](https://en.wikipedia.org/wiki/Fuchsia_\(operating_system\) "Fuchsia \(operating system\)")
  * _[Glass OS](https://en.wikipedia.org/wiki/Glass_OS "Glass OS")_
  * _[Google TV](https://en.wikipedia.org/wiki/Google_TV_\(2010%E2%80%932014\) "Google TV \(2010–2014\)")_
  * [gLinux](https://en.wikipedia.org/wiki/GLinux "GLinux")
  * _[Goobuntu](https://en.wikipedia.org/wiki/Goobuntu "Goobuntu")_
  * [Wear OS](https://en.wikipedia.org/wiki/Wear_OS "Wear OS")

 |  
| Machine learning models  | 
  * BERT
  * [Chinchilla](https://en.wikipedia.org/wiki/Chinchilla_\(language_model\) "Chinchilla \(language model\)")
  * [DreamBooth](https://en.wikipedia.org/wiki/DreamBooth "DreamBooth")
  * [Gemini](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini \(language model\)")
  * [Gemini Robotics](https://en.wikipedia.org/wiki/Gemini_Robotics "Gemini Robotics")
  * [Gemma](https://en.wikipedia.org/wiki/Gemma_\(language_model\) "Gemma \(language model\)")
  * [Imagen](https://en.wikipedia.org/wiki/Imagen_\(text-to-image_model\) "Imagen \(text-to-image model\)") (2023)
  * [LaMDA](https://en.wikipedia.org/wiki/LaMDA "LaMDA")
  * [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM")
  * [T5](https://en.wikipedia.org/wiki/T5_\(language_model\) "T5 \(language model\)")
  * [Veo (text-to-video model)](https://en.wikipedia.org/wiki/Veo_\(text-to-video_model\) "Veo \(text-to-video model\)")
  * [VideoPoet](https://en.wikipedia.org/wiki/VideoPoet "VideoPoet")
  * _[XLNet](https://en.wikipedia.org/wiki/XLNet "XLNet")_

 |  
| Neural networks  | 
  * [EfficientNet](https://en.wikipedia.org/wiki/EfficientNet "EfficientNet")
  * [Gato](https://en.wikipedia.org/wiki/Gato_\(DeepMind\) "Gato \(DeepMind\)")
  * [Inception](https://en.wikipedia.org/wiki/Inception_\(deep_learning_architecture\) "Inception \(deep learning architecture\)")
  * [MobileNet](https://en.wikipedia.org/wiki/MobileNet "MobileNet")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\) "Transformer \(deep learning architecture\)")
  * [WaveNet](https://en.wikipedia.org/wiki/WaveNet "WaveNet")

 |  
| Computer programs  | 
  * [AlphaDev](https://en.wikipedia.org/wiki/AlphaDev "AlphaDev")
  * [AlphaFold](https://en.wikipedia.org/wiki/AlphaFold "AlphaFold")
  * [AlphaGeometry](https://en.wikipedia.org/wiki/AlphaGeometry "AlphaGeometry")
  * [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo "AlphaGo")
  * [AlphaGo Zero](https://en.wikipedia.org/wiki/AlphaGo_Zero "AlphaGo Zero")
  * [AlphaStar](https://en.wikipedia.org/wiki/AlphaStar_\(software\) "AlphaStar \(software\)")
  * [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero "AlphaZero")
  * [Master](https://en.wikipedia.org/wiki/Master_\(software\) "Master \(software\)")
  * [MuZero](https://en.wikipedia.org/wiki/MuZero "MuZero")

 |  
| Formats and codecs  | 
  * [AAB](https://en.wikipedia.org/wiki/Android_App_Bundle "Android App Bundle")
  * [APK](https://en.wikipedia.org/wiki/Apk_\(file_format\) "Apk \(file format\)")
  * [AV1](https://en.wikipedia.org/wiki/AV1 "AV1")
  * [iLBC](https://en.wikipedia.org/wiki/Internet_Low_Bitrate_Codec "Internet Low Bitrate Codec")
  * [iSAC](https://en.wikipedia.org/wiki/Internet_Speech_Audio_Codec "Internet Speech Audio Codec")
  * [libvpx](https://en.wikipedia.org/wiki/Libvpx "Libvpx")
  * [Lyra](https://en.wikipedia.org/wiki/Lyra_\(codec\) "Lyra \(codec\)")
  * [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers "Protocol Buffers")
  * [Ultra HDR](https://en.wikipedia.org/wiki/Ultra_HDR "Ultra HDR")
  * [VP3](https://en.wikipedia.org/wiki/VP3 "VP3")
  * [VP6](https://en.wikipedia.org/wiki/VP6 "VP6")
  * [VP8](https://en.wikipedia.org/wiki/VP8 "VP8")
  * [VP9](https://en.wikipedia.org/wiki/VP9 "VP9")
  * [WebM](https://en.wikipedia.org/wiki/WebM "WebM")
  * [WebP](https://en.wikipedia.org/wiki/WebP "WebP")
  * [WOFF2](https://en.wikipedia.org/wiki/Web_Open_Font_Format "Web Open Font Format")

 |  
| Programming languages  | 
  * [Carbon](https://en.wikipedia.org/wiki/Carbon_\(programming_language\) "Carbon \(programming language\)")
  * [Dart](https://en.wikipedia.org/wiki/Dart_\(programming_language\) "Dart \(programming language\)")
  * [Go](https://en.wikipedia.org/wiki/Go_\(programming_language\) "Go \(programming language\)")
  * _[Sawzall](https://en.wikipedia.org/wiki/Sawzall_\(programming_language\) "Sawzall \(programming language\)")_

 |  
| Search algorithms  | 
  * [Googlebot](https://en.wikipedia.org/wiki/Googlebot "Googlebot")
  * [Hummingbird](https://en.wikipedia.org/wiki/Google_Hummingbird "Google Hummingbird")
  * [Mobilegeddon](https://en.wikipedia.org/wiki/Mobilegeddon "Mobilegeddon")
  * [PageRank](https://en.wikipedia.org/wiki/PageRank "PageRank")
    * [matrix](https://en.wikipedia.org/wiki/Google_matrix "Google matrix")
  * [Panda](https://en.wikipedia.org/wiki/Google_Panda "Google Panda")
  * [Penguin](https://en.wikipedia.org/wiki/Google_Penguin "Google Penguin")
  * [Pigeon](https://en.wikipedia.org/wiki/Google_Pigeon "Google Pigeon")
  * [RankBrain](https://en.wikipedia.org/wiki/RankBrain "RankBrain")

 |  
| [Domain names](https://en.wikipedia.org/wiki/Category:Google_domain_names "Category:Google domain names")  | 
  * [.app](https://en.wikipedia.org/wiki/.app_\(top-level_domain\) ".app \(top-level domain\)")
  * [.dev](https://en.wikipedia.org/wiki/.dev ".dev")
  * [.google](https://en.wikipedia.org/wiki/.google ".google")
  * [.zip](https://en.wikipedia.org/wiki/.zip_\(top-level_domain\) ".zip \(top-level domain\)")
  * [g.co](https://en.wikipedia.org/wiki/G.co "G.co")
  * [google.by](https://en.wikipedia.org/wiki/Google.by "Google.by")

 |  
| Typefaces  | 
  * [Croscore](https://en.wikipedia.org/wiki/Croscore_fonts "Croscore fonts")
  * [Noto](https://en.wikipedia.org/wiki/Noto_fonts "Noto fonts")
  * [Product Sans](https://en.wikipedia.org/wiki/Product_Sans "Product Sans")
  * [Roboto](https://en.wikipedia.org/wiki/Roboto "Roboto")

 |  
 |  
 |  
|   
 | [Software](https://en.wikipedia.org/wiki/List_of_Google_products "List of Google products") |  
| --- |  
|   
 | A  | 
  * _[Aardvark](https://en.wikipedia.org/wiki/Aardvark_\(search_engine\) "Aardvark \(search engine\)")_
  * [Account](https://en.wikipedia.org/wiki/Google_Account "Google Account")
    * [Dashboard](https://en.wikipedia.org/wiki/Google_Dashboard "Google Dashboard")
    * [Takeout](https://en.wikipedia.org/wiki/Google_Takeout "Google Takeout")
  * [Ad Manager](https://en.wikipedia.org/wiki/Google_Ad_Manager "Google Ad Manager")
  * [AdMob](https://en.wikipedia.org/wiki/AdMob "AdMob")
  * [Ads](https://en.wikipedia.org/wiki/Google_Ads "Google Ads")
  * [AdSense](https://en.wikipedia.org/wiki/Google_AdSense "Google AdSense")
  * _[Affiliate Network](https://en.wikipedia.org/wiki/Google_Affiliate_Network "Google Affiliate Network")_
  * [Alerts](https://en.wikipedia.org/wiki/Google_Alerts "Google Alerts")
  * _[Allo](https://en.wikipedia.org/wiki/Google_Allo "Google Allo")_
  * [Analytics](https://en.wikipedia.org/wiki/Google_Analytics "Google Analytics")
  * [Android Auto](https://en.wikipedia.org/wiki/Android_Auto "Android Auto")
  * _[Android Beam](https://en.wikipedia.org/wiki/Android_Beam "Android Beam")_
  * _[Answers](https://en.wikipedia.org/wiki/Google_Answers "Google Answers")_
  * _[Apture](https://en.wikipedia.org/wiki/Apture "Apture")_
  * [Arts & Culture](https://en.wikipedia.org/wiki/Google_Arts_%26_Culture "Google Arts & Culture")
  * [Assistant](https://en.wikipedia.org/wiki/Google_Assistant "Google Assistant")
  * _[Attribution](https://en.wikipedia.org/wiki/Google_Attribution "Google Attribution")_
  * [Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator "Google Authenticator")

 |  
| --- | --- |  
| B  | 
  * _[BebaPay](https://en.wikipedia.org/wiki/BebaPay "BebaPay")_
  * _[BeatThatQuote.com](https://en.wikipedia.org/wiki/BeatThatQuote.com "BeatThatQuote.com")_
  * [Beam](https://en.wikipedia.org/wiki/Google_Beam "Google Beam")
  * _[Blog Search](https://en.wikipedia.org/wiki/Google_Blog_Search "Google Blog Search")_
  * [Blogger](https://en.wikipedia.org/wiki/Blogger_\(service\) "Blogger \(service\)")
  * _[Body](https://en.wikipedia.org/wiki/ZygoteBody "ZygoteBody")_
  * _[Bookmarks](https://en.wikipedia.org/wiki/Google_Bookmarks "Google Bookmarks")_
  * [Books](https://en.wikipedia.org/wiki/Google_Books "Google Books")
    * [Ngram Viewer](https://en.wikipedia.org/wiki/Google_Books_Ngram_Viewer "Google Books Ngram Viewer")
  * _[Browser Sync](https://en.wikipedia.org/wiki/Google_Browser_Sync "Google Browser Sync")_
  * _[Building Maker](https://en.wikipedia.org/wiki/Google_Building_Maker "Google Building Maker")_
  * _[Bump](https://en.wikipedia.org/wiki/Bump_\(application\) "Bump \(application\)")_
  * _[BumpTop](https://en.wikipedia.org/wiki/BumpTop "BumpTop")_
  * _[Buzz](https://en.wikipedia.org/wiki/Google_Buzz "Google Buzz")_

 |  
| C  | 
  * [Calendar](https://en.wikipedia.org/wiki/Google_Calendar "Google Calendar")
  * [Cast](https://en.wikipedia.org/wiki/Google_Cast "Google Cast")
  * _[Catalogs](https://en.wikipedia.org/wiki/Google_Catalogs "Google Catalogs")_
  * [Chat](https://en.wikipedia.org/wiki/Google_Chat "Google Chat")
  * _[Checkout](https://en.wikipedia.org/wiki/Google_Checkout "Google Checkout")_
  * [Chrome](https://en.wikipedia.org/wiki/Google_Chrome "Google Chrome")
  * _[Chrome Apps](https://en.wikipedia.org/wiki/Google_Chrome_App "Google Chrome App")_
  * [Chrome Experiments](https://en.wikipedia.org/wiki/Google_Chrome_Experiments "Google Chrome Experiments")
  * [Chrome Remote Desktop](https://en.wikipedia.org/wiki/Chrome_Remote_Desktop "Chrome Remote Desktop")
  * [Chrome Web Store](https://en.wikipedia.org/wiki/Chrome_Web_Store "Chrome Web Store")
  * [Classroom](https://en.wikipedia.org/wiki/Google_Classroom "Google Classroom")
  * _[Cloud Print](https://en.wikipedia.org/wiki/Google_Cloud_Print "Google Cloud Print")_
  * [Cloud Search](https://en.wikipedia.org/wiki/Google_Cloud_Search "Google Cloud Search")
  * [Contacts](https://en.wikipedia.org/wiki/Google_Contacts "Google Contacts")
  * _[Contributor](https://en.wikipedia.org/wiki/Google_Contributor "Google Contributor")_
  * [Crowdsource](https://en.wikipedia.org/wiki/Crowdsource_\(app\) "Crowdsource \(app\)")
  * _[Currents](https://en.wikipedia.org/wiki/Google_Currents_\(social_app\) "Google Currents \(social app\)")_ (social app)
  * _[Currents](https://en.wikipedia.org/wiki/Google_Currents_\(news_app\) "Google Currents \(news app\)")_ (news app)

 |  
| D  | 
  * [Data Commons](https://en.wikipedia.org/wiki/Data_Commons "Data Commons")
  * [Dataset Search](https://en.wikipedia.org/wiki/Google_Dataset_Search "Google Dataset Search")
  * _[Desktop](https://en.wikipedia.org/wiki/Google_Desktop "Google Desktop")_
  * [Dictionary](https://en.wikipedia.org/wiki/Google_Dictionary "Google Dictionary")
  * [Dinosaur Game](https://en.wikipedia.org/wiki/Dinosaur_Game "Dinosaur Game")
  * _[Directory](https://en.wikipedia.org/wiki/Google_Directory "Google Directory")_
  * [Docs](https://en.wikipedia.org/wiki/Google_Docs "Google Docs")
  * [Docs Editors](https://en.wikipedia.org/wiki/Google_Docs_Editors "Google Docs Editors")
  * _[Domains](https://en.wikipedia.org/wiki/Google_Domains "Google Domains")_
  * [Drawings](https://en.wikipedia.org/wiki/Google_Drawings "Google Drawings")
  * [Drive](https://en.wikipedia.org/wiki/Google_Drive "Google Drive")
  * _[Duo](https://en.wikipedia.org/wiki/Google_Duo "Google Duo")_

 |  
| E  | 
  * [Earth](https://en.wikipedia.org/wiki/Google_Earth "Google Earth")
  * [Etherpad](https://en.wikipedia.org/wiki/Etherpad "Etherpad")
  * _[Expeditions](https://en.wikipedia.org/wiki/Google_Expeditions "Google Expeditions")_
  * _[Express](https://en.wikipedia.org/wiki/Google_Express "Google Express")_

 |  
| F  | 
  * [Family Link](https://en.wikipedia.org/wiki/Google_Family_Link "Google Family Link")
  * _[Fast Flip](https://en.wikipedia.org/wiki/Google_Fast_Flip "Google Fast Flip")_
  * [FeedBurner](https://en.wikipedia.org/wiki/FeedBurner "FeedBurner")
  * _[fflick](https://en.wikipedia.org/wiki/Fflick "Fflick")_
  * [Fi Wireless](https://en.wikipedia.org/wiki/Google_Fi_Wireless "Google Fi Wireless")
  * [Finance](https://en.wikipedia.org/wiki/Google_Finance "Google Finance")
  * [Files](https://en.wikipedia.org/wiki/Files_\(Google\) "Files \(Google\)")
  * [Find Hub](https://en.wikipedia.org/wiki/Find_Hub "Find Hub")
  * _[Fit](https://en.wikipedia.org/wiki/Google_Fit "Google Fit")_
  * [Flights](https://en.wikipedia.org/wiki/Google_Flights "Google Flights")
  * _[Flu Trends](https://en.wikipedia.org/wiki/Google_Flu_Trends "Google Flu Trends")_
  * [Fonts](https://en.wikipedia.org/wiki/Google_Fonts "Google Fonts")
  * [Forms](https://en.wikipedia.org/wiki/Google_Forms "Google Forms")
  * _[Friend Connect](https://en.wikipedia.org/wiki/Google_Friend_Connect "Google Friend Connect")_
  * _[Fusion Tables](https://en.wikipedia.org/wiki/Google_Fusion_Tables "Google Fusion Tables")_

 |  
| G  | 
  * [Gboard](https://en.wikipedia.org/wiki/Gboard "Gboard")
  * [Gemini](https://en.wikipedia.org/wiki/Google_Gemini "Google Gemini")
    * [Nano Banana](https://en.wikipedia.org/wiki/Nano_Banana "Nano Banana")
  * _[Gesture Search](https://en.wikipedia.org/wiki/Google_Gesture_Search "Google Gesture Search")_
  * _[Gizmo5](https://en.wikipedia.org/wiki/Gizmo5 "Gizmo5")_
  * _[Google+](https://en.wikipedia.org/wiki/Google%2B "Google+")_
  * [Gmail](https://en.wikipedia.org/wiki/Gmail "Gmail")
  * _[Goggles](https://en.wikipedia.org/wiki/Google_Goggles "Google Goggles")_
  * _[GOOG-411](https://en.wikipedia.org/wiki/GOOG-411 "GOOG-411")_
  * _[Grasshopper](https://en.wikipedia.org/wiki/Grasshopper_\(mobile_app\) "Grasshopper \(mobile app\)")_
  * [Groups](https://en.wikipedia.org/wiki/Google_Groups "Google Groups")

 |  
| H  | 
  * _[Hangouts](https://en.wikipedia.org/wiki/Google_Hangouts "Google Hangouts")_
  * _[Helpouts](https://en.wikipedia.org/wiki/Google_Helpouts "Google Helpouts")_
  * [Home](https://en.wikipedia.org/wiki/Google_Home_\(platform\) "Google Home \(platform\)")

 |  
| I  | 
  * _[iGoogle](https://en.wikipedia.org/wiki/IGoogle "IGoogle")_
  * [Images](https://en.wikipedia.org/wiki/Google_Images "Google Images")
    * _[Image Labeler](https://en.wikipedia.org/wiki/Google_Image_Labeler "Google Image Labeler")_
  * _[Image Swirl](https://en.wikipedia.org/wiki/Google_Image_Swirl "Google Image Swirl")_
  * _[Inbox by Gmail](https://en.wikipedia.org/wiki/Inbox_by_Gmail "Inbox by Gmail")_
  * [Input Tools](https://en.wikipedia.org/wiki/Google_Input_Tools "Google Input Tools")
    * [Japanese Input](https://en.wikipedia.org/wiki/Google_Japanese_Input "Google Japanese Input")
    * _[Pinyin](https://en.wikipedia.org/wiki/Google_Pinyin "Google Pinyin")_
  * _[Insights for Search](https://en.wikipedia.org/wiki/Google_Insights_for_Search "Google Insights for Search")_

 |  
| J  | 
  * _[Jaiku](https://en.wikipedia.org/wiki/Jaiku "Jaiku")_
  * _[Jamboard](https://en.wikipedia.org/wiki/Jamboard "Jamboard")_

 |  
| K  | 
  * [Kaggle](https://en.wikipedia.org/wiki/Kaggle "Kaggle")
  * [Keep](https://en.wikipedia.org/wiki/Google_Keep "Google Keep")
  * _[Knol](https://en.wikipedia.org/wiki/Knol "Knol")_

 |  
| L  | 
  * [Labs](https://en.wikipedia.org/wiki/Google_Labs "Google Labs")
  * _[Latitude](https://en.wikipedia.org/wiki/Google_Latitude "Google Latitude")_
  * [Lens](https://en.wikipedia.org/wiki/Google_Lens "Google Lens")
  * _[Like.com](https://en.wikipedia.org/wiki/Like.com "Like.com")_
  * [Live Transcribe](https://en.wikipedia.org/wiki/Live_Transcribe "Live Transcribe")
  * _[Lively](https://en.wikipedia.org/wiki/Google_Lively "Google Lively")_

 |  
| M  | 
  * _[Map Maker](https://en.wikipedia.org/wiki/Google_Map_Maker "Google Map Maker")_
  * [Maps](https://en.wikipedia.org/wiki/Google_Maps "Google Maps")
  * _[Maps Navigation](https://en.wikipedia.org/wiki/Google_Maps_Navigation "Google Maps Navigation")_
  * [Marketing Platform](https://en.wikipedia.org/wiki/Google_Marketing_Platform "Google Marketing Platform")
  * [Meet](https://en.wikipedia.org/wiki/Google_Meet "Google Meet")
  * [Messages](https://en.wikipedia.org/wiki/Google_Messages "Google Messages")
  * _[Moderator](https://en.wikipedia.org/wiki/Google_Moderator "Google Moderator")_
  * _[My Tracks](https://en.wikipedia.org/wiki/My_Tracks "My Tracks")_

 |  
| N  | 
  * _[Nearby Share](https://en.wikipedia.org/wiki/Nearby_Share "Nearby Share")_
  * [News](https://en.wikipedia.org/wiki/Google_News "Google News")
  * _[News& Weather](https://en.wikipedia.org/wiki/Google_News_%26_Weather "Google News & Weather")_
  * [News Archive](https://en.wikipedia.org/wiki/Google_News_Archive "Google News Archive")
  * _[Notebook](https://en.wikipedia.org/wiki/Google_Notebook "Google Notebook")_
  * [NotebookLM](https://en.wikipedia.org/wiki/NotebookLM "NotebookLM")
  * _[Now](https://en.wikipedia.org/wiki/Google_Now "Google Now")_

 |  
| O  | 
  * _[Offers](https://en.wikipedia.org/wiki/Google_Offers "Google Offers")_
  * [One](https://en.wikipedia.org/wiki/Google_One "Google One")
  * _[One Pass](https://en.wikipedia.org/wiki/Google_One_Pass "Google One Pass")_
  * [Opinion Rewards](https://en.wikipedia.org/wiki/Google_Opinion_Rewards "Google Opinion Rewards")
  * _[Orkut](https://en.wikipedia.org/wiki/Orkut "Orkut")_
  * _[Oyster](https://en.wikipedia.org/wiki/Oyster_\(company\) "Oyster \(company\)")_

 |  
| P  | 
  * _[Panoramio](https://en.wikipedia.org/wiki/Panoramio "Panoramio")_
  * _[PaperofRecord.com](https://en.wikipedia.org/wiki/PaperofRecord.com "PaperofRecord.com")_
  * [Patents](https://en.wikipedia.org/wiki/Google_Patents "Google Patents")
  * _[Page Creator](https://en.wikipedia.org/wiki/Google_Page_Creator "Google Page Creator")_
  * _[Pay](https://en.wikipedia.org/wiki/Google_Pay_\(mobile_app\) "Google Pay \(mobile app\)")_ (mobile app)
  * [Pay](https://en.wikipedia.org/wiki/Google_Pay_\(payment_method\) "Google Pay \(payment method\)") (payment method)
  * _[Pay Send](https://en.wikipedia.org/wiki/Google_Pay_Send "Google Pay Send")_
  * [People Cards](https://en.wikipedia.org/wiki/People_Cards "People Cards")
  * [Person Finder](https://en.wikipedia.org/wiki/Google_Person_Finder "Google Person Finder")
  * _[Personalized Search](https://en.wikipedia.org/wiki/Google_Personalized_Search "Google Personalized Search")_
  * [Photomath](https://en.wikipedia.org/wiki/Photomath "Photomath")
  * [Photos](https://en.wikipedia.org/wiki/Google_Photos "Google Photos")
  * _[Picasa](https://en.wikipedia.org/wiki/Picasa "Picasa")_
  * _[Picasa Web Albums](https://en.wikipedia.org/wiki/Picasa_Web_Albums "Picasa Web Albums")_
  * _[Picnik](https://en.wikipedia.org/wiki/Picnik "Picnik")_
  * [Pixel Camera](https://en.wikipedia.org/wiki/Pixel_Camera "Pixel Camera")
  * [Play](https://en.wikipedia.org/wiki/Google_Play "Google Play")
  * [Play Books](https://en.wikipedia.org/wiki/Google_Play_Books "Google Play Books")
  * [Play Games](https://en.wikipedia.org/wiki/Google_Play_Games "Google Play Games")
  * _[Play Music](https://en.wikipedia.org/wiki/Google_Play_Music "Google Play Music")_
  * _[Play Newsstand](https://en.wikipedia.org/wiki/Google_Play_Newsstand "Google Play Newsstand")_
  * [Play Pass](https://en.wikipedia.org/wiki/Google_Play_Pass "Google Play Pass")
  * [Play Services](https://en.wikipedia.org/wiki/Google_Play_Services "Google Play Services")
  * _[Podcasts](https://en.wikipedia.org/wiki/Google_Podcasts "Google Podcasts")_
  * _[Poly](https://en.wikipedia.org/wiki/Poly_\(website\) "Poly \(website\)")_
  * _[Postini](https://en.wikipedia.org/wiki/Postini "Postini")_
  * _[PostRank](https://en.wikipedia.org/wiki/PostRank "PostRank")_
  * _[Primer](https://en.wikipedia.org/wiki/Google_Primer "Google Primer")_
  * [Public Alerts](https://en.wikipedia.org/wiki/Google_Public_Alerts "Google Public Alerts")
  * _[Public Data Explorer](https://en.wikipedia.org/wiki/Google_Public_Data_Explorer "Google Public Data Explorer")_

 |  
| Q  | 
  * [Question Hub](https://en.wikipedia.org/wiki/Google_Question_Hub "Google Question Hub")
  * [Quick, Draw!](https://en.wikipedia.org/wiki/Quick,_Draw! "Quick, Draw!")
  * _[Quick Search Box](https://en.wikipedia.org/wiki/Google_Quick_Search_Box "Google Quick Search Box")_
  * [Quick Share](https://en.wikipedia.org/wiki/Quick_Share "Quick Share")
  * _[Quickoffice](https://en.wikipedia.org/wiki/Quickoffice "Quickoffice")_

 |  
| R  | 
  * [Read Along](https://en.wikipedia.org/wiki/Read_Along "Read Along")
  * _[Reader](https://en.wikipedia.org/wiki/Google_Reader "Google Reader")_
  * _[Reply](https://en.wikipedia.org/wiki/Reply_\(Google\) "Reply \(Google\)")_

 |  
| S  | 
  * [Safe Browsing](https://en.wikipedia.org/wiki/Google_Safe_Browsing "Google Safe Browsing")
  * [SageTV](https://en.wikipedia.org/wiki/SageTV "SageTV")
  * [Santa Tracker](https://en.wikipedia.org/wiki/Google_Santa_Tracker "Google Santa Tracker")
  * _[Schemer](https://en.wikipedia.org/wiki/Google_Schemer "Google Schemer")_
  * [Scholar](https://en.wikipedia.org/wiki/Google_Scholar "Google Scholar")
  * [Search](https://en.wikipedia.org/wiki/Google_Search "Google Search")
    * [AI Overviews](https://en.wikipedia.org/wiki/AI_Overviews "AI Overviews")
    * [Knowledge Graph](https://en.wikipedia.org/wiki/Knowledge_Graph_\(Google\) "Knowledge Graph \(Google\)")
    * [SafeSearch](https://en.wikipedia.org/wiki/SafeSearch "SafeSearch")
  * _[Searchwiki](https://en.wikipedia.org/wiki/Google_SearchWiki "Google SearchWiki")_
  * [Sheets](https://en.wikipedia.org/wiki/Google_Sheets "Google Sheets")
  * _[Shoploop](https://en.wikipedia.org/wiki/Shoploop "Shoploop")_
  * [Shopping](https://en.wikipedia.org/wiki/Google_Shopping "Google Shopping")
  * _[Sidewiki](https://en.wikipedia.org/wiki/Google_Sidewiki "Google Sidewiki")_
  * [Sites](https://en.wikipedia.org/wiki/Google_Sites "Google Sites")
  * [Slides](https://en.wikipedia.org/wiki/Google_Slides "Google Slides")
  * [Snapseed](https://en.wikipedia.org/wiki/Snapseed "Snapseed")
  * _[Socratic](https://en.wikipedia.org/wiki/Socratic_\(Google\) "Socratic \(Google\)")_
  * _[Softcard](https://en.wikipedia.org/wiki/Softcard "Softcard")_
  * _[Songza](https://en.wikipedia.org/wiki/Songza "Songza")_
  * [Sound Amplifier](https://en.wikipedia.org/wiki/Sound_Amplifier "Sound Amplifier")
  * _[Spaces](https://en.wikipedia.org/wiki/Google_Spaces "Google Spaces")_
  * [Sparrow](https://en.wikipedia.org/wiki/Sparrow_\(chatbot\) "Sparrow \(chatbot\)") (chatbot)
  * _[Sparrow](https://en.wikipedia.org/wiki/Sparrow_\(email_client\) "Sparrow \(email client\)")_ (email client)
  * [Speech Recognition & Synthesis](https://en.wikipedia.org/wiki/Speech_Recognition_%26_Synthesis "Speech Recognition & Synthesis")
  * _[Squared](https://en.wikipedia.org/wiki/Google_Squared "Google Squared")_
  * _[Stadia](https://en.wikipedia.org/wiki/Google_Stadia "Google Stadia")_
  * _[Station](https://en.wikipedia.org/wiki/Google_Station "Google Station")_
  * [Store](https://en.wikipedia.org/wiki/Google_Store "Google Store")
  * [Street View](https://en.wikipedia.org/wiki/Google_Street_View "Google Street View")
  * _[Surveys](https://en.wikipedia.org/wiki/Google_Surveys "Google Surveys")_
  * _[Sync](https://en.wikipedia.org/wiki/Google_Sync "Google Sync")_

 |  
| T  | 
  * _[Tables](https://en.wikipedia.org/wiki/Tables_\(Google\) "Tables \(Google\)")_
  * _[Talk](https://en.wikipedia.org/wiki/Google_Talk "Google Talk")_
  * [TalkBack](https://en.wikipedia.org/wiki/TalkBack "TalkBack")
  * [Tasks](https://en.wikipedia.org/wiki/Google_Tasks "Google Tasks")
  * [Tenor](https://en.wikipedia.org/wiki/Tenor_\(website\) "Tenor \(website\)")
  * _[Tez](https://en.wikipedia.org/wiki/Tez_\(software\) "Tez \(software\)")_
  * _[Tilt Brush](https://en.wikipedia.org/wiki/Tilt_Brush "Tilt Brush")_
  * _[Toolbar](https://en.wikipedia.org/wiki/Google_Toolbar "Google Toolbar")_
  * [Toontastic 3D](https://en.wikipedia.org/wiki/Toontastic_3D "Toontastic 3D")
  * [Translate](https://en.wikipedia.org/wiki/Google_Translate "Google Translate")
  * [Travel](https://en.wikipedia.org/wiki/Google_Travel "Google Travel")
  * _[Trendalyzer](https://en.wikipedia.org/wiki/Trendalyzer "Trendalyzer")_
  * [Trends](https://en.wikipedia.org/wiki/Google_Trends "Google Trends")
  * [TV](https://en.wikipedia.org/wiki/Google_TV_\(service\) "Google TV \(service\)")

 |  
| U  | 
  * _[URL Shortener](https://en.wikipedia.org/wiki/Google_URL_Shortener "Google URL Shortener")_

 |  
| V  | 
  * _[Video](https://en.wikipedia.org/wiki/Google_Video "Google Video")_
  * [Vids](https://en.wikipedia.org/wiki/Google_Vids "Google Vids")
  * [Voice](https://en.wikipedia.org/wiki/Google_Voice "Google Voice")
  * [Voice Access](https://en.wikipedia.org/wiki/Voice_Access "Voice Access")
  * [Voice Search](https://en.wikipedia.org/wiki/Google_Voice_Search "Google Voice Search")

 |  
| W  | 
  * [Wallet](https://en.wikipedia.org/wiki/Google_Wallet "Google Wallet")
  * _[Wave](https://en.wikipedia.org/wiki/Google_Wave "Google Wave")_
  * [Waze](https://en.wikipedia.org/wiki/Waze "Waze")
  * _[WDYL](https://en.wikipedia.org/wiki/WDYL_\(search_engine\) "WDYL \(search engine\)")_
  * _[Web Light](https://en.wikipedia.org/wiki/Google_Web_Light "Google Web Light")_
  * [Where Is My Train](https://en.wikipedia.org/wiki/Where_Is_My_Train "Where Is My Train")
  * [Widevine](https://en.wikipedia.org/wiki/Widevine "Widevine")
  * [Wiz](https://en.wikipedia.org/wiki/Wiz,_Inc. "Wiz, Inc.")
  * _[Word Lens](https://en.wikipedia.org/wiki/Word_Lens "Word Lens")_
  * [Workspace](https://en.wikipedia.org/wiki/Google_Workspace "Google Workspace")
  * [Workspace Marketplace](https://en.wikipedia.org/wiki/Google_Workspace_Marketplace "Google Workspace Marketplace")

 |  
| Y  | 
  * [YouTube](https://en.wikipedia.org/wiki/YouTube "YouTube")
  * [YouTube Kids](https://en.wikipedia.org/wiki/YouTube_Kids "YouTube Kids")
  * [YouTube Music](https://en.wikipedia.org/wiki/YouTube_Music "YouTube Music")
  * [YouTube Premium](https://en.wikipedia.org/wiki/YouTube_Premium "YouTube Premium")
  * [YouTube Shorts](https://en.wikipedia.org/wiki/YouTube_Shorts "YouTube Shorts")
  * [YouTube Studio](https://en.wikipedia.org/wiki/YouTube_Studio "YouTube Studio")
  * [YouTube TV](https://en.wikipedia.org/wiki/YouTube_TV "YouTube TV")
  * [YouTube VR](https://en.wikipedia.org/wiki/YouTube_VR "YouTube VR")

 |  
 |  
 |  
|   
 | Hardware |  
| --- |  
|   
 | [Pixel](https://en.wikipedia.org/wiki/Google_Pixel "Google Pixel")  |   
 | [Smartphones](https://en.wikipedia.org/wiki/Comparison_of_Google_Pixel_smartphones "Comparison of Google Pixel smartphones")  | 
  * [Pixel](https://en.wikipedia.org/wiki/Pixel_\(1st_generation\) "Pixel \(1st generation\)") (2016)
  * [Pixel 2](https://en.wikipedia.org/wiki/Pixel_2 "Pixel 2") (2017)
  * [Pixel 3](https://en.wikipedia.org/wiki/Pixel_3 "Pixel 3") (2018)
  * [Pixel 3a](https://en.wikipedia.org/wiki/Pixel_3a "Pixel 3a") (2019)
  * [Pixel 4](https://en.wikipedia.org/wiki/Pixel_4 "Pixel 4") (2019)
  * [Pixel 4a](https://en.wikipedia.org/wiki/Pixel_4a "Pixel 4a") (2020)
  * [Pixel 5](https://en.wikipedia.org/wiki/Pixel_5 "Pixel 5") (2020)
  * [Pixel 5a](https://en.wikipedia.org/wiki/Pixel_5a "Pixel 5a") (2021)
  * [Pixel 6](https://en.wikipedia.org/wiki/Pixel_6 "Pixel 6") (2021)
  * [Pixel 6a](https://en.wikipedia.org/wiki/Pixel_6a "Pixel 6a") (2022)
  * [Pixel 7](https://en.wikipedia.org/wiki/Pixel_7 "Pixel 7") (2022)
  * [Pixel 7a](https://en.wikipedia.org/wiki/Pixel_7a "Pixel 7a") (2023)
  * [Pixel Fold](https://en.wikipedia.org/wiki/Pixel_Fold "Pixel Fold") (2023)
  * [Pixel 8](https://en.wikipedia.org/wiki/Pixel_8 "Pixel 8") (2023)
  * [Pixel 8a](https://en.wikipedia.org/wiki/Pixel_8a "Pixel 8a") (2024)
  * [Pixel 9](https://en.wikipedia.org/wiki/Pixel_9 "Pixel 9") (2024)
  * [Pixel 9 Pro Fold](https://en.wikipedia.org/wiki/Pixel_9_Pro_Fold "Pixel 9 Pro Fold") (2024)
  * [Pixel 9a](https://en.wikipedia.org/wiki/Pixel_9a "Pixel 9a") (2025)
  * [Pixel 10](https://en.wikipedia.org/wiki/Pixel_10 "Pixel 10") (2025)
  * [Pixel 10 Pro Fold](https://en.wikipedia.org/wiki/Pixel_10_Pro_Fold "Pixel 10 Pro Fold") (2025)

 |  
| --- | --- |  
| Smartwatches  | 
  * [Pixel Watch](https://en.wikipedia.org/wiki/Pixel_Watch "Pixel Watch") (2022)
  * [Pixel Watch 2](https://en.wikipedia.org/wiki/Pixel_Watch_2 "Pixel Watch 2") (2023)
  * [Pixel Watch 3](https://en.wikipedia.org/wiki/Pixel_Watch_3 "Pixel Watch 3") (2024)
  * [Pixel Watch 4](https://en.wikipedia.org/wiki/Pixel_Watch_4 "Pixel Watch 4") (2025)

 |  
| Tablets  | 
  * [Pixel C](https://en.wikipedia.org/wiki/Pixel_C "Pixel C") (2015)
  * [Pixel Slate](https://en.wikipedia.org/wiki/Pixel_Slate "Pixel Slate") (2018)
  * [Pixel Tablet](https://en.wikipedia.org/wiki/Pixel_Tablet "Pixel Tablet") (2023)

 |  
| Laptops  | 
  * [Chromebook Pixel](https://en.wikipedia.org/wiki/Chromebook_Pixel "Chromebook Pixel") (2013–2015)
  * [Pixelbook](https://en.wikipedia.org/wiki/Pixelbook "Pixelbook") (2017)
  * [Pixelbook Go](https://en.wikipedia.org/wiki/Pixelbook_Go "Pixelbook Go") (2019)

 |  
| Other  | 
  * [Pixel Buds](https://en.wikipedia.org/wiki/Pixel_Buds "Pixel Buds") (2017–present)

 |  
 |  
| [Nexus](https://en.wikipedia.org/wiki/Google_Nexus "Google Nexus")  |   
 | [Smartphones](https://en.wikipedia.org/wiki/Comparison_of_Google_Nexus_smartphones "Comparison of Google Nexus smartphones")  | 
  * [Nexus One](https://en.wikipedia.org/wiki/Nexus_One "Nexus One") (2010)
  * [Nexus S](https://en.wikipedia.org/wiki/Nexus_S "Nexus S") (2010)
  * [Galaxy Nexus](https://en.wikipedia.org/wiki/Galaxy_Nexus "Galaxy Nexus") (2011)
  * [Nexus 4](https://en.wikipedia.org/wiki/Nexus_4 "Nexus 4") (2012)
  * [Nexus 5](https://en.wikipedia.org/wiki/Nexus_5 "Nexus 5") (2013)
  * [Nexus 6](https://en.wikipedia.org/wiki/Nexus_6 "Nexus 6") (2014)
  * [Nexus 5X](https://en.wikipedia.org/wiki/Nexus_5X "Nexus 5X") (2015)
  * [Nexus 6P](https://en.wikipedia.org/wiki/Nexus_6P "Nexus 6P") (2015)

 |  
| --- | --- |  
| [Tablets](https://en.wikipedia.org/wiki/Comparison_of_Google_Nexus_tablets "Comparison of Google Nexus tablets")  | 
  * [Nexus 7](https://en.wikipedia.org/wiki/Nexus_7_\(2012\) "Nexus 7 \(2012\)") (2012)
  * [Nexus 10](https://en.wikipedia.org/wiki/Nexus_10 "Nexus 10") (2012)
  * [Nexus 7](https://en.wikipedia.org/wiki/Nexus_7_\(2013\) "Nexus 7 \(2013\)") (2013)
  * [Nexus 9](https://en.wikipedia.org/wiki/Nexus_9 "Nexus 9") (2014)

 |  
| Other  | 
  * [Nexus Q](https://en.wikipedia.org/wiki/Nexus_Q "Nexus Q") (2012)
  * [Nexus Player](https://en.wikipedia.org/wiki/Nexus_Player "Nexus Player") (2014)

 |  
 |  
| Other  | 
  * _[Android Dev Phone](https://en.wikipedia.org/wiki/Android_Dev_Phone "Android Dev Phone")_
  * [Android One](https://en.wikipedia.org/wiki/Android_One "Android One")
  * _[Cardboard](https://en.wikipedia.org/wiki/Google_Cardboard "Google Cardboard")_
  * [Chromebit](https://en.wikipedia.org/wiki/Chromebit "Chromebit")
  * [Chromebook](https://en.wikipedia.org/wiki/Chromebook "Chromebook")
  * [Chromebox](https://en.wikipedia.org/wiki/Chromebox "Chromebox")
  * [Chromecast](https://en.wikipedia.org/wiki/Chromecast "Chromecast")
  * [Clips](https://en.wikipedia.org/wiki/Google_Clips "Google Clips")
  * [Daydream](https://en.wikipedia.org/wiki/Google_Daydream "Google Daydream")
  * [Fitbit](https://en.wikipedia.org/wiki/List_of_Fitbit_products "List of Fitbit products")
  * [Glass](https://en.wikipedia.org/wiki/Google_Glass "Google Glass")
  * [Liftware](https://en.wikipedia.org/wiki/Liftware "Liftware")
  * [Liquid Galaxy](https://en.wikipedia.org/wiki/Liquid_Galaxy "Liquid Galaxy")
  * [Nest](https://en.wikipedia.org/wiki/Google_Nest "Google Nest")
    * [smart speakers](https://en.wikipedia.org/wiki/Google_Nest_\(smart_speakers\) "Google Nest \(smart speakers\)")
    * [Thermostat](https://en.wikipedia.org/wiki/Nest_Thermostat "Nest Thermostat")
    * [Wifi](https://en.wikipedia.org/wiki/Nest_Wifi "Nest Wifi")
  * _[Play Edition](https://en.wikipedia.org/wiki/List_of_Google_Play_edition_devices "List of Google Play edition devices")_
  * _[Project Ara](https://en.wikipedia.org/wiki/Project_Ara "Project Ara")_
  * _[OnHub](https://en.wikipedia.org/wiki/Google_OnHub "Google OnHub")_
  * _[Pixel Visual Core](https://en.wikipedia.org/wiki/Pixel_Visual_Core "Pixel Visual Core")_
  * [Project Iris](https://en.wikipedia.org/wiki/Project_Iris "Project Iris")
  * _[Search Appliance](https://en.wikipedia.org/wiki/Google_Search_Appliance "Google Search Appliance")_
  * [Sycamore processor](https://en.wikipedia.org/wiki/Sycamore_processor "Sycamore processor")
  * [Tensor](https://en.wikipedia.org/wiki/Google_Tensor "Google Tensor")
  * [Tensor Processing Unit](https://en.wikipedia.org/wiki/Tensor_Processing_Unit "Tensor Processing Unit")
  * [Titan Security Key](https://en.wikipedia.org/wiki/Titan_Security_Key "Titan Security Key")

 |  
 |  
 |  
|   
 | 
  * [v](https://en.wikipedia.org/wiki/Template:Google_litigation "Template:Google litigation")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Google_litigation "Template talk:Google litigation")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Google_litigation "Special:EditPage/Template:Google litigation")

[Litigation](https://en.wikipedia.org/wiki/Google_litigation "Google litigation")  |  
| --- |  
| Advertising  | 
  * _[Feldman v. Google, Inc.](https://en.wikipedia.org/wiki/Feldman_v._Google,_Inc. "Feldman v. Google, Inc.")_ (2007)
  * _[Rescuecom Corp. v. Google Inc.](https://en.wikipedia.org/wiki/Rescuecom_Corp._v._Google_Inc. "Rescuecom Corp. v. Google Inc.")_ (2009)
  * _[Goddard v. Google, Inc.](https://en.wikipedia.org/wiki/Goddard_v._Google,_Inc. "Goddard v. Google, Inc.")_ (2009)
  * _[Rosetta Stone Ltd. v. Google, Inc.](https://en.wikipedia.org/wiki/Rosetta_Stone_Ltd._v._Google,_Inc. "Rosetta Stone Ltd. v. Google, Inc.")_ (2012)
  * _[Google, Inc. v. American Blind& Wallpaper Factory, Inc.](https://en.wikipedia.org/wiki/Google,_Inc._v._American_Blind_%26_Wallpaper_Factory,_Inc. "Google, Inc. v. American Blind & Wallpaper Factory, Inc.")_ (2017)
  * [Jedi Blue](https://en.wikipedia.org/wiki/Jedi_Blue "Jedi Blue")

 |  
| Antitrust  | 
  * [European Union](https://en.wikipedia.org/wiki/Antitrust_cases_against_Google_by_the_European_Union "Antitrust cases against Google by the European Union") (2010–present)
  * _[United States v. Adobe Systems, Inc., Apple Inc., Google Inc., Intel Corporation, Intuit, Inc., and Pixar](https://en.wikipedia.org/wiki/High-Tech_Employee_Antitrust_Litigation "High-Tech Employee Antitrust Litigation")_ (2011)
  * _[Umar Javeed, Sukarma Thapar, Aaqib Javeed vs. Google LLC and Ors.](https://en.wikipedia.org/wiki/Umar_Javeed,_Sukarma_Thapar,_Aaqib_Javeed_vs._Google_LLC_and_Ors. "Umar Javeed, Sukarma Thapar, Aaqib Javeed vs. Google LLC and Ors.")_ (2019)
  * _[United States v. Google LLC](https://en.wikipedia.org/wiki/United_States_v._Google_LLC_\(2020\) "United States v. Google LLC \(2020\)")_ (2020)
  * _[Epic Games v. Google](https://en.wikipedia.org/wiki/Epic_Games_v._Google "Epic Games v. Google")_ (2021)
  * _[United States v. Google LLC](https://en.wikipedia.org/wiki/United_States_v._Google_LLC_\(2023\) "United States v. Google LLC \(2023\)")_ (2023)

 |  
| Intellectual  
property  | 
  * _[Perfect 10, Inc. v. Amazon.com, Inc.](https://en.wikipedia.org/wiki/Perfect_10,_Inc._v._Amazon.com,_Inc. "Perfect 10, Inc. v. Amazon.com, Inc.")_ (2007)
  * _[Viacom International, Inc. v. YouTube, Inc.](https://en.wikipedia.org/wiki/Viacom_International,_Inc._v._YouTube,_Inc. "Viacom International, Inc. v. YouTube, Inc.")_ (2010)
  * _[Lenz v. Universal Music Corp.](https://en.wikipedia.org/wiki/Lenz_v._Universal_Music_Corp. "Lenz v. Universal Music Corp.")_(2015)
  * _[Authors Guild, Inc. v. Google, Inc.](https://en.wikipedia.org/wiki/Authors_Guild,_Inc._v._Google,_Inc. "Authors Guild, Inc. v. Google, Inc.")_ (2015)
  * _[Field v. Google, Inc.](https://en.wikipedia.org/wiki/Field_v._Google,_Inc. "Field v. Google, Inc.")_ (2016)
  * _[Google LLC v. Oracle America, Inc.](https://en.wikipedia.org/wiki/Google_LLC_v._Oracle_America,_Inc. "Google LLC v. Oracle America, Inc.")_ (2021)
  * [Smartphone patent wars](https://en.wikipedia.org/wiki/Smartphone_patent_wars "Smartphone patent wars")

 |  
| Privacy  | 
  * _[Rocky Mountain Bank v. Google, Inc.](https://en.wikipedia.org/wiki/Rocky_Mountain_Bank_v._Google,_Inc. "Rocky Mountain Bank v. Google, Inc.")_ (2009)
  * _[Hibnick v. Google, Inc.](https://en.wikipedia.org/wiki/Hibnick_v._Google,_Inc. "Hibnick v. Google, Inc.")_ (2010)
  * _[United States v. Google Inc.](https://en.wikipedia.org/wiki/United_States_v._Google_Inc. "United States v. Google Inc.")_ (2012)
  * [Judgement of the German Federal Court of Justice on Google's autocomplete function](https://en.wikipedia.org/wiki/Judgement_of_the_German_Federal_Court_of_Justice_on_Google%27s_autocomplete_function "Judgement of the German Federal Court of Justice on Google's autocomplete function") (2013)
  * _[Joffe v. Google, Inc.](https://en.wikipedia.org/wiki/Joffe_v._Google,_Inc. "Joffe v. Google, Inc.")_ (2013)
  * _[Mosley v SARL Google](https://en.wikipedia.org/wiki/Mosley_v_SARL_Google "Mosley v SARL Google")_ (2013)
  * _[Google Spain v AEPD and Mario Costeja González](https://en.wikipedia.org/wiki/Google_Spain_v_AEPD_and_Mario_Costeja_Gonz%C3%A1lez "Google Spain v AEPD and Mario Costeja González")_ (2014)
  * _[Frank v. Gaos](https://en.wikipedia.org/wiki/Frank_v._Gaos "Frank v. Gaos")_ (2019)

 |  
| Other  | 
  * _[Garcia v. Google, Inc.](https://en.wikipedia.org/wiki/Garcia_v._Google,_Inc. "Garcia v. Google, Inc.")_ (2015)
  * _[Google LLC v Defteros](https://en.wikipedia.org/wiki/Google_LLC_v_Defteros "Google LLC v Defteros")_ (2020)
  * _[Gonzalez v. Google LLC](https://en.wikipedia.org/wiki/Gonzalez_v._Google_LLC "Gonzalez v. Google LLC")_ (2022)

 |  
 |  
|   
 | Related |  
| --- |  
|   
 | Concepts  | 
  * [Beauty YouTuber](https://en.wikipedia.org/wiki/Beauty_YouTuber "Beauty YouTuber")
  * [BookTube](https://en.wikipedia.org/wiki/BookTube "BookTube")
  * [BreadTube](https://en.wikipedia.org/wiki/BreadTube "BreadTube")
  * "[Don't be evil](https://en.wikipedia.org/wiki/Don%27t_be_evil "Don't be evil")"
  * [Gayglers](https://en.wikipedia.org/wiki/Gayglers "Gayglers")
  * [_Google_ as a verb](https://en.wikipedia.org/wiki/Google_\(verb\) "Google \(verb\)")
  * [Google bombing](https://en.wikipedia.org/wiki/Google_bombing "Google bombing")
    * [2004 U.S. presidential election](https://en.wikipedia.org/wiki/Political_Google_bombs_in_the_2004_U.S._presidential_election "Political Google bombs in the 2004 U.S. presidential election")
  * [Google effect](https://en.wikipedia.org/wiki/Google_effect "Google effect")
  * [Googlefight](https://en.wikipedia.org/wiki/Googlefight "Googlefight")
  * [Google hacking](https://en.wikipedia.org/wiki/Google_hacking "Google hacking")
  * [Googleshare](https://en.wikipedia.org/wiki/Googleshare "Googleshare")
  * [Google tax](https://en.wikipedia.org/wiki/Google_tax "Google tax")
  * [Googlewhack](https://en.wikipedia.org/wiki/Googlewhack "Googlewhack")
  * [Googlization](https://en.wikipedia.org/wiki/Googlization "Googlization")
  * [Illegal flower tribute](https://en.wikipedia.org/wiki/Illegal_flower_tribute "Illegal flower tribute")
  * [Objectives and key results](https://en.wikipedia.org/wiki/Objectives_and_key_results "Objectives and key results")
  * [Rooting](https://en.wikipedia.org/wiki/Rooting_\(Android\) "Rooting \(Android\)")
  * [Search engine manipulation effect](https://en.wikipedia.org/wiki/Search_engine_manipulation_effect "Search engine manipulation effect")
  * [Side project time](https://en.wikipedia.org/wiki/Side_project_time "Side project time")
  * [Sitelink](https://en.wikipedia.org/wiki/Sitelink "Sitelink")
  * [Site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering "Site reliability engineering")
  * [StudyTube](https://en.wikipedia.org/wiki/StudyTube "StudyTube")
  * [VTuber](https://en.wikipedia.org/wiki/VTuber "VTuber")
  * [YouTube Poop](https://en.wikipedia.org/wiki/YouTube_Poop "YouTube Poop")
  * [YouTuber](https://en.wikipedia.org/wiki/YouTuber "YouTuber")
    * [list](https://en.wikipedia.org/wiki/List_of_YouTubers "List of YouTubers")

 |  
| --- | --- |  
| Products  |   
 | Android  | 
  * [Booting process](https://en.wikipedia.org/wiki/Booting_process_of_Android_devices "Booting process of Android devices")
  * [Custom distributions](https://en.wikipedia.org/wiki/List_of_custom_Android_distributions "List of custom Android distributions")
  * [Features](https://en.wikipedia.org/wiki/List_of_features_in_Android "List of features in Android")
  * [Recovery mode](https://en.wikipedia.org/wiki/Android_recovery_mode "Android recovery mode")
  * [Software development](https://en.wikipedia.org/wiki/Android_software_development "Android software development")

 |  
| --- | --- |  
| [Street View coverage](https://en.wikipedia.org/wiki/Google_Street_View_coverage "Google Street View coverage")  | 
  * [Africa](https://en.wikipedia.org/wiki/Google_Street_View_in_Africa "Google Street View in Africa")
  * [Antarctica](https://en.wikipedia.org/wiki/Google_Street_View_in_Antarctica "Google Street View in Antarctica")
  * [Asia](https://en.wikipedia.org/wiki/Google_Street_View_in_Asia "Google Street View in Asia")
    * [Israel](https://en.wikipedia.org/wiki/Google_Street_View_in_Israel "Google Street View in Israel")
  * [Europe](https://en.wikipedia.org/wiki/Google_Street_View_in_Europe "Google Street View in Europe")
  * [North America](https://en.wikipedia.org/wiki/Google_Street_View_in_North_America "Google Street View in North America")
    * [Canada](https://en.wikipedia.org/wiki/Google_Street_View_in_Canada "Google Street View in Canada")
    * [United States](https://en.wikipedia.org/wiki/Google_Street_View_in_the_United_States "Google Street View in the United States")
  * [Oceania](https://en.wikipedia.org/wiki/Google_Street_View_in_Oceania "Google Street View in Oceania")
  * [South America](https://en.wikipedia.org/wiki/Google_Street_View_in_South_America "Google Street View in South America")
    * [Argentina](https://en.wikipedia.org/wiki/Google_Street_View_in_Argentina "Google Street View in Argentina")
    * [Chile](https://en.wikipedia.org/wiki/Google_Street_View_in_Chile "Google Street View in Chile")
    * [Colombia](https://en.wikipedia.org/wiki/Google_Street_View_in_Colombia "Google Street View in Colombia")

 |  
| YouTube  | 
  * [Copyright strike](https://en.wikipedia.org/wiki/YouTube_copyright_strike "YouTube copyright strike")
  * [Education](https://en.wikipedia.org/wiki/YouTube_in_education "YouTube in education")
  * [Features](https://en.wikipedia.org/wiki/List_of_YouTube_features "List of YouTube features")
  * [Moderation](https://en.wikipedia.org/wiki/YouTube_moderation "YouTube moderation")
  * [Most-disliked videos](https://en.wikipedia.org/wiki/List_of_most-disliked_YouTube_videos "List of most-disliked YouTube videos")
  * [Most-liked videos](https://en.wikipedia.org/wiki/List_of_most-liked_YouTube_videos "List of most-liked YouTube videos")
  * [Most-subscribed channels](https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels "List of most-subscribed YouTube channels")
  * [Most-viewed channels](https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_channels "List of most-viewed YouTube channels")
  * [Most-viewed videos](https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos "List of most-viewed YouTube videos")
  * [Official channel](https://en.wikipedia.org/wiki/YouTube_\(YouTube_channel\) "YouTube \(YouTube channel\)")
  * [Social impact](https://en.wikipedia.org/wiki/Social_impact_of_YouTube "Social impact of YouTube")
  * [YouTube Premium original programming](https://en.wikipedia.org/wiki/List_of_YouTube_Premium_original_programming "List of YouTube Premium original programming")

 |  
| Other  | 
  * [Gmail interface](https://en.wikipedia.org/wiki/Gmail_interface "Gmail interface")
  * [Maps pin](https://en.wikipedia.org/wiki/Google_Maps_pin "Google Maps pin")
  * [Most downloaded Google Play applications](https://en.wikipedia.org/wiki/List_of_most-downloaded_Google_Play_applications "List of most-downloaded Google Play applications")
  * [Stadia games](https://en.wikipedia.org/wiki/List_of_Stadia_games "List of Stadia games")

 |  
 |  
| [Documentaries](https://en.wikipedia.org/wiki/Category:Documentary_films_about_Google "Category:Documentary films about Google")  | 
  * _[AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_\(film\) "AlphaGo \(film\)")_
  * _[Google: Behind the Screen](https://en.wikipedia.org/wiki/Google_Behind_the_Screen "Google Behind the Screen")_
  * _[Google Maps Road Trip](https://en.wikipedia.org/wiki/Google_Maps_Road_Trip "Google Maps Road Trip")_
  * _[Google and the World Brain](https://en.wikipedia.org/wiki/Google_and_the_World_Brain "Google and the World Brain")_
  * _[The Creepy Line](https://en.wikipedia.org/wiki/The_Creepy_Line "The Creepy Line")_

 |  
| [Books](https://en.wikipedia.org/wiki/Category:Books_about_Google "Category:Books about Google")  | 
  * _[Google Hacks](https://en.wikipedia.org/wiki/Google_Hacks "Google Hacks")_
  * _[The Google Story](https://en.wikipedia.org/wiki/The_Google_Story "The Google Story")_
  * _[Googled: The End of the World as We Know It](https://en.wikipedia.org/wiki/Googled:_The_End_of_the_World_as_We_Know_It "Googled: The End of the World as We Know It")_
  * _[How Google Works](https://en.wikipedia.org/wiki/How_Google_Works "How Google Works")_
  * _[I'm Feeling Lucky](https://en.wikipedia.org/wiki/I%27m_Feeling_Lucky_\(book\) "I'm Feeling Lucky \(book\)")_
  * _[In the Plex](https://en.wikipedia.org/wiki/In_the_Plex "In the Plex")_
  * _[The MANIAC](https://en.wikipedia.org/wiki/The_MANIAC "The MANIAC")_

 |  
| Popular culture  | 
  * _[Google Feud](https://en.wikipedia.org/wiki/Google_Feud "Google Feud")_
  * _[Google Me](https://en.wikipedia.org/wiki/Google_Me_\(film\) "Google Me \(film\)")_ (film)
  * "[Google Me](https://en.wikipedia.org/wiki/Google_Me_\(Kim_Zolciak_song\) "Google Me \(Kim Zolciak song\)")" (Kim Zolciak song)
  * "[Google Me](https://en.wikipedia.org/wiki/Google_Me_\(Teyana_Taylor_song\) "Google Me \(Teyana Taylor song\)")" (Teyana Taylor song)
  * _[Is Google Making Us Stupid?](https://en.wikipedia.org/wiki/Is_Google_Making_Us_Stupid%3F "Is Google Making Us Stupid?")_
  * _[Proceratium google](https://en.wikipedia.org/wiki/Proceratium_google "Proceratium google")_
  * _[Matt Nathanson: Live at Google](https://en.wikipedia.org/wiki/Matt_Nathanson:_Live_at_Google "Matt Nathanson: Live at Google")_
  * _[The Billion Dollar Code](https://en.wikipedia.org/wiki/The_Billion_Dollar_Code "The Billion Dollar Code")_
  * _[The Internship](https://en.wikipedia.org/wiki/The_Internship "The Internship")_
  * _[Where on Google Earth is Carmen Sandiego?](https://en.wikipedia.org/wiki/Where_on_Google_Earth_is_Carmen_Sandiego%3F "Where on Google Earth is Carmen Sandiego?")_

 |  
| Other  | 
  * "[Attention Is All You Need](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need "Attention Is All You Need")"
  * [elgooG](https://en.wikipedia.org/wiki/ElgooG "ElgooG")
  * [Generative pre-trained transformer](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
  * "[Me at the zoo](https://en.wikipedia.org/wiki/Me_at_the_zoo "Me at the zoo")"
  * [Predictions of the end](https://en.wikipedia.org/wiki/Predictions_of_the_end_of_Google "Predictions of the end of Google")
  * [Relationship with Wikipedia](https://en.wikipedia.org/wiki/Relationship_between_Google_and_Wikipedia "Relationship between Google and Wikipedia")
  * "[Reunion](https://en.wikipedia.org/wiki/Reunion_\(advertisement\) "Reunion \(advertisement\)")"
  * [Robot Constitution](https://en.wikipedia.org/wiki/Robot_Constitution "Robot Constitution")

 |  
 |  
 |  
|  _Italics_ denote [discontinued products](https://en.wikipedia.org/wiki/List_of_Google_products#Discontinued_products_and_services "List of Google products"). 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category](https://en.wikipedia.org/wiki/Category:Google "Category:Google")
  * ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Global_thinking.svg/20px-Global_thinking.svg.png) [Outline](https://en.wikipedia.org/wiki/Outline_of_Google "Outline of Google")

 |  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Large_language_models "Template:Large language models")
  * [t](https://en.wikipedia.org/w/index.php?title=Template_talk:Large_language_models&action=edit&redlink=1 "Template talk:Large language models \(page does not exist\)")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Large_language_models "Special:EditPage/Template:Large language models")

[Large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") (LLMs)  |  
| --- |  
| 
  * [List of LLMs](https://en.wikipedia.org/wiki/List_of_large_language_models "List of large language models")
  * [AI Companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies "List of artificial intelligence companies")
  * [Benchmarks](https://en.wikipedia.org/wiki/Language_model_benchmark "Language model benchmark")
  * [List of chatbots](https://en.wikipedia.org/wiki/List_of_chatbots "List of chatbots")
  * [Foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model")
  * [Generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence "Generative artificial intelligence")

 |  
| Concepts  | 
  * [Language model](https://en.wikipedia.org/wiki/Language_model "Language model")
  * [NLP](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing")
  * [NLG](https://en.wikipedia.org/wiki/Natural_language_generation "Natural language generation")
  * [Computational linguistics](https://en.wikipedia.org/wiki/Computational_linguistics "Computational linguistics")
  * [Foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model")
  * [Small language model](https://en.wikipedia.org/wiki/Small_language_model "Small language model")
  * [Reasoning model](https://en.wikipedia.org/wiki/Reasoning_model "Reasoning model")
  * [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning\) "Transformer \(deep learning\)")
    * [Attention](https://en.wikipedia.org/wiki/Attention_\(machine_learning\) "Attention \(machine learning\)")
    * [KV cache](https://en.wikipedia.org/wiki/Transformer_\(deep_learning\)#KV_caching "Transformer \(deep learning\)")
  * [Context window](https://en.wikipedia.org/wiki/Context_window "Context window")
  * [Tokenization](https://en.wikipedia.org/wiki/Large_language_model#Tokenization "Large language model")
  * [Word embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding")
  * [Parameter](https://en.wikipedia.org/wiki/Parameter "Parameter")
  * [Hyperparameter](https://en.wikipedia.org/wiki/Hyperparameter_\(machine_learning\) "Hyperparameter \(machine learning\)")
  * [Autoregression](https://en.wikipedia.org/wiki/Autoregressive_model "Autoregressive model")
  * [Mixture of experts (MoE)](https://en.wikipedia.org/wiki/Mixture_of_experts "Mixture of experts")
  * [Inference](https://en.wikipedia.org/wiki/Inference_\(machine_learning\) "Inference \(machine learning\)")
  * [Model compression](https://en.wikipedia.org/wiki/Model_compression "Model compression")
    * [Knowledge distillation](https://en.wikipedia.org/wiki/Knowledge_distillation "Knowledge distillation")
  * [Speculative decoding](https://en.wikipedia.org/wiki/Speculative_decoding "Speculative decoding")
  * [PagedAttention](https://en.wikipedia.org/wiki/PagedAttention "PagedAttention")
  * [Neural scaling law](https://en.wikipedia.org/wiki/Neural_scaling_law "Neural scaling law")
  * [Multimodality](https://en.wikipedia.org/wiki/Multimodal_learning "Multimodal learning")

 |  
| Training, prompting, and alignment  | 
  * [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning")
  * [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning "Supervised learning")
  * [Fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(machine_learning\) "Fine-tuning \(machine learning\)")
    * [Instruction tuning](https://en.wikipedia.org/wiki/Instruction_tuning "Instruction tuning")
  * [RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")
  * [Constitutional AI](https://en.wikipedia.org/wiki/Constitutional_AI "Constitutional AI")
  * [AI alignment](https://en.wikipedia.org/wiki/AI_alignment "AI alignment")
  * [AI safety](https://en.wikipedia.org/wiki/AI_safety "AI safety")
  * [Mechanistic interpretability](https://en.wikipedia.org/wiki/Mechanistic_interpretability "Mechanistic interpretability")
  * [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering")
    * [In-context learning](https://en.wikipedia.org/wiki/In-context_learning "In-context learning")
    * [Chain-of-thought prompting](https://en.wikipedia.org/wiki/Chain-of-thought_prompting "Chain-of-thought prompting")
  * [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation "Retrieval-augmented generation")
  * [Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection "Prompt injection")
  * [Adversarial machine learning](https://en.wikipedia.org/wiki/Adversarial_machine_learning "Adversarial machine learning")
  * [Hallucination](https://en.wikipedia.org/wiki/Hallucination_\(artificial_intelligence\) "Hallucination \(artificial intelligence\)")
  * [Stochastic parrot](https://en.wikipedia.org/wiki/Stochastic_parrot "Stochastic parrot")
  * [Glitch token](https://en.wikipedia.org/wiki/Glitch_token "Glitch token")

 |  
| Models  |   
 | Early and encoder models  | 
  * [Word2vec](https://en.wikipedia.org/wiki/Word2vec "Word2vec")
  * [Seq2seq](https://en.wikipedia.org/wiki/Seq2seq "Seq2seq")
  * [GloVe](https://en.wikipedia.org/wiki/GloVe "GloVe")
  * BERT
  * [XLNet](https://en.wikipedia.org/wiki/XLNet "XLNet")
  * [T5](https://en.wikipedia.org/wiki/T5_\(language_model\) "T5 \(language model\)")

 |  
| --- | --- |  
| GPT series  | 
  * [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
    * [GPT-1](https://en.wikipedia.org/wiki/GPT-1 "GPT-1")
    * [GPT-2](https://en.wikipedia.org/wiki/GPT-2 "GPT-2")
    * [GPT-3](https://en.wikipedia.org/wiki/GPT-3 "GPT-3")
    * [GPT-4](https://en.wikipedia.org/wiki/GPT-4 "GPT-4")
    * [GPT-4.1](https://en.wikipedia.org/wiki/GPT-4.1 "GPT-4.1")
    * [GPT-4.5](https://en.wikipedia.org/wiki/GPT-4.5 "GPT-4.5")
    * [GPT-4o](https://en.wikipedia.org/wiki/GPT-4o "GPT-4o")
    * [GPT-5](https://en.wikipedia.org/wiki/GPT-5 "GPT-5")
    * [GPT-5.5](https://en.wikipedia.org/wiki/GPT-5.5 "GPT-5.5")
  * [Codex](https://en.wikipedia.org/wiki/OpenAI_Codex_\(language_model\) "OpenAI Codex \(language model\)")
  * [OpenAI o1](https://en.wikipedia.org/wiki/OpenAI_o1 "OpenAI o1")
  * [OpenAI o3](https://en.wikipedia.org/wiki/OpenAI_o3 "OpenAI o3")
  * [OpenAI o4-mini](https://en.wikipedia.org/wiki/OpenAI_o4-mini "OpenAI o4-mini")

 |  
| Other model families  | 
  * [BLOOM](https://en.wikipedia.org/wiki/BLOOM_\(language_model\) "BLOOM \(language model\)")
  * [Chinchilla](https://en.wikipedia.org/wiki/Chinchilla_\(language_model\) "Chinchilla \(language model\)")
  * [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\) "Claude \(language model\)")
  * [DBRX](https://en.wikipedia.org/wiki/DBRX "DBRX")
  * [Gemini](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini \(language model\)")
    * [Gemma](https://en.wikipedia.org/wiki/Gemma_\(language_model\) "Gemma \(language model\)")
  * [GPT-J](https://en.wikipedia.org/wiki/GPT-J "GPT-J")
  * [PanGu](https://en.wikipedia.org/wiki/Huawei_PanGu "Huawei PanGu")
  * [Granite](https://en.wikipedia.org/wiki/IBM_Granite "IBM Granite")
  * [Jais](https://en.wikipedia.org/wiki/Jais_\(language_model\) "Jais \(language model\)")
  * [LaMDA](https://en.wikipedia.org/wiki/LaMDA "LaMDA")
  * [Llama](https://en.wikipedia.org/wiki/Llama_\(language_model\) "Llama \(language model\)")
    * [Vicuna](https://en.wikipedia.org/wiki/Vicuna_LLM "Vicuna LLM")
  * [Minerva](https://en.wikipedia.org/wiki/Minerva_\(model\) "Minerva \(model\)")
  * [Mistral and Mixtral](https://en.wikipedia.org/wiki/Mistral_AI#Models "Mistral AI")
  * [Nemotron](https://en.wikipedia.org/wiki/Nemotron "Nemotron")
  * [PaLM](https://en.wikipedia.org/wiki/PaLM "PaLM")
  * [Phi](https://en.wikipedia.org/wiki/Phi_\(language_model\) "Phi \(language model\)")
  * [Qwen](https://en.wikipedia.org/wiki/Qwen "Qwen")
  * [Xiaomi MiMo](https://en.wikipedia.org/wiki/Xiaomi_MiMo "Xiaomi MiMo")

 |  
 |  
| Chatbots and assistants  | 
  * [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT")
  * [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\) "Claude \(language model\)")
  * [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek_\(chatbot\) "DeepSeek \(chatbot\)")
  * [Ernie Bot](https://en.wikipedia.org/wiki/Ernie_Bot "Ernie Bot")
  * [Gemini](https://en.wikipedia.org/wiki/Gemini_\(chatbot\) "Gemini \(chatbot\)")
  * [Grok](https://en.wikipedia.org/wiki/Grok_\(chatbot\) "Grok \(chatbot\)")
  * [Microsoft Copilot](https://en.wikipedia.org/wiki/Microsoft_Copilot "Microsoft Copilot")
  * [Meta AI](https://en.wikipedia.org/wiki/Meta_AI "Meta AI")
  * [Perplexity AI](https://en.wikipedia.org/wiki/Perplexity_AI "Perplexity AI")
  * [Sparrow](https://en.wikipedia.org/wiki/Sparrow_\(chatbot\) "Sparrow \(chatbot\)")
  * [You.com](https://en.wikipedia.org/wiki/You.com "You.com")

 |  
| Agents, coding, and applications  | 
  * [AI agent](https://en.wikipedia.org/wiki/AI_agent "AI agent")
  * [Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent "Intelligent agent")
  * [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT "AutoGPT")
  * [CrewAI](https://en.wikipedia.org/wiki/CrewAI "CrewAI")
  * [LangChain](https://en.wikipedia.org/wiki/LangChain "LangChain")
  * [Manus](https://en.wikipedia.org/wiki/Manus_\(AI_agent\) "Manus \(AI agent\)")
  * [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol "Model Context Protocol")
  * [Agent2Agent](https://en.wikipedia.org/wiki/Agent2Agent "Agent2Agent")
  * [OpenAI Codex](https://en.wikipedia.org/wiki/OpenAI_Codex_\(AI_agent\) "OpenAI Codex \(AI agent\)")
  * [Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding "Vibe coding")
  * [Code generation](https://en.wikipedia.org/wiki/AI-assisted_software_development "AI-assisted software development")
  * [Question answering](https://en.wikipedia.org/wiki/Question_answering "Question answering")
  * [Machine translation](https://en.wikipedia.org/wiki/Machine_translation "Machine translation")
  * [Text summarization](https://en.wikipedia.org/wiki/Text_summarization "Text summarization")
  * [Chatbot](https://en.wikipedia.org/wiki/Chatbot "Chatbot")
  * [Virtual assistant](https://en.wikipedia.org/wiki/Virtual_assistant "Virtual assistant")
  * [LLMs in higher education](https://en.wikipedia.org/wiki/LLMs_in_higher_education "LLMs in higher education")

 |  
| Software  | 
  * [PyTorch](https://en.wikipedia.org/wiki/PyTorch "PyTorch")
  * [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow "TensorFlow")
  * [Hugging Face](https://en.wikipedia.org/wiki/Hugging_Face "Hugging Face")
  * [Inference engine](https://en.wikipedia.org/wiki/Inference_engine "Inference engine")
  * [llama.cpp](https://en.wikipedia.org/wiki/Llama.cpp "Llama.cpp")
  * [Ollama](https://en.wikipedia.org/wiki/Ollama "Ollama")
  * [SGLang](https://en.wikipedia.org/wiki/SGLang "SGLang")
  * [TensorRT-LLM](https://en.wikipedia.org/wiki/TensorRT#TensorRT-LLM "TensorRT")
  * [vLLM](https://en.wikipedia.org/wiki/VLLM "VLLM")
  * [ONNX](https://en.wikipedia.org/wiki/Open_Neural_Network_Exchange "Open Neural Network Exchange")
  * [OpenVINO](https://en.wikipedia.org/wiki/OpenVINO "OpenVINO")
  * [Vector database](https://en.wikipedia.org/wiki/Vector_database "Vector database")
  * [ChromaDB](https://en.wikipedia.org/wiki/ChromaDB "ChromaDB")
  * [Deep learning software](https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software "Comparison of deep learning software")
  * [Open-source AI software](https://en.wikipedia.org/wiki/Lists_of_open-source_artificial_intelligence_software "Lists of open-source artificial intelligence software")

 |  
| Hardware and infrastructure  | 
  * [AI data center](https://en.wikipedia.org/wiki/AI_data_center "AI data center")
  * [AI accelerator](https://en.wikipedia.org/wiki/AI_accelerator "AI accelerator")
  * [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit "Graphics processing unit")
  * [CUDA](https://en.wikipedia.org/wiki/CUDA "CUDA")
  * [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit "Tensor Processing Unit")
  * [High-bandwidth memory](https://en.wikipedia.org/wiki/High_Bandwidth_Memory "High Bandwidth Memory")

 |  
| Benchmarks, evaluation, and detection  | 
  * [Language model benchmark](https://en.wikipedia.org/wiki/Language_model_benchmark "Language model benchmark")
  * [MMLU](https://en.wikipedia.org/wiki/MMLU "MMLU")
  * [Humanity's Last Exam](https://en.wikipedia.org/wiki/Humanity%27s_Last_Exam "Humanity's Last Exam")
  * [LMArena](https://en.wikipedia.org/wiki/LMArena "LMArena")
  * [LLM-as-a-Judge](https://en.wikipedia.org/wiki/LLM-as-a-Judge "LLM-as-a-Judge")
  * [Perplexity metric](https://en.wikipedia.org/wiki/Perplexity#Token-normalized_perplexity "Perplexity")
  * [GPTZero](https://en.wikipedia.org/wiki/GPTZero "GPTZero")
  * [Artificial intelligence content detection](https://en.wikipedia.org/wiki/Artificial_intelligence_content_detection "Artificial intelligence content detection")
  * [Undetectable.ai](https://en.wikipedia.org/wiki/Undetectable.ai "Undetectable.ai")

 |  
| Datasets and data  | 
  * [Data set](https://en.wikipedia.org/wiki/Data_set "Data set")
  * [Text corpus](https://en.wikipedia.org/wiki/Text_corpus "Text corpus")
  * [Common Crawl](https://en.wikipedia.org/wiki/Common_Crawl "Common Crawl")
  * [The Pile](https://en.wikipedia.org/wiki/The_Pile_\(dataset\) "The Pile \(dataset\)")
  * [Web scraping](https://en.wikipedia.org/wiki/Web_scraping "Web scraping")
  * [Synthetic data](https://en.wikipedia.org/wiki/Synthetic_data "Synthetic data")
  * [Training, validation, and test data sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets "Training, validation, and test data sets")

 |  
| Organizations  | 
  * [AI21 Labs](https://en.wikipedia.org/wiki/AI21_Labs "AI21 Labs")
  * [Alibaba Group](https://en.wikipedia.org/wiki/Alibaba_Group "Alibaba Group")
  * [Anthropic](https://en.wikipedia.org/wiki/Anthropic "Anthropic")
  * [Baidu](https://en.wikipedia.org/wiki/Baidu "Baidu")
  * [Cohere](https://en.wikipedia.org/wiki/Cohere "Cohere")
  * [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek "DeepSeek")
  * [EleutherAI](https://en.wikipedia.org/wiki/EleutherAI "EleutherAI")
  * [Google DeepMind](https://en.wikipedia.org/wiki/Google_DeepMind "Google DeepMind")
  * [Hugging Face](https://en.wikipedia.org/wiki/Hugging_Face "Hugging Face")
  * [Meta AI](https://en.wikipedia.org/wiki/Meta_AI "Meta AI")
  * [Microsoft AI](https://en.wikipedia.org/wiki/Microsoft_AI "Microsoft AI")
  * [Mistral AI](https://en.wikipedia.org/wiki/Mistral_AI "Mistral AI")
  * [Nvidia](https://en.wikipedia.org/wiki/Nvidia "Nvidia")
  * [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI")
  * [Technology Innovation Institute](https://en.wikipedia.org/wiki/Technology_Innovation_Institute "Technology Innovation Institute")
  * [xAI](https://en.wikipedia.org/wiki/XAI_\(company\) "XAI \(company\)")

 |  
| People  | 
  * [Sam Altman](https://en.wikipedia.org/wiki/Sam_Altman "Sam Altman")
  * [Dario Amodei](https://en.wikipedia.org/wiki/Dario_Amodei "Dario Amodei")
  * [Yoshua Bengio](https://en.wikipedia.org/wiki/Yoshua_Bengio "Yoshua Bengio")
  * [Aidan Gomez](https://en.wikipedia.org/wiki/Aidan_Gomez "Aidan Gomez")
  * [Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis "Demis Hassabis")
  * [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton "Geoffrey Hinton")
  * [Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy "Andrej Karpathy")
  * [Yann LeCun](https://en.wikipedia.org/wiki/Yann_LeCun "Yann LeCun")
  * [Percy Liang](https://en.wikipedia.org/wiki/Percy_Liang "Percy Liang")
  * [Christopher D. Manning](https://en.wikipedia.org/wiki/Christopher_D._Manning "Christopher D. Manning")
  * [Arthur Mensch](https://en.wikipedia.org/wiki/Arthur_Mensch "Arthur Mensch")
  * [Mira Murati](https://en.wikipedia.org/wiki/Mira_Murati "Mira Murati")
  * [Alec Radford](https://en.wikipedia.org/wiki/Alec_Radford "Alec Radford")
  * [Noam Shazeer](https://en.wikipedia.org/wiki/Noam_Shazeer "Noam Shazeer")
  * [Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever "Ilya Sutskever")
  * [Ashish Vaswani](https://en.wikipedia.org/wiki/Ashish_Vaswani "Ashish Vaswani")
  * [Andrew Ng](https://en.wikipedia.org/wiki/Andrew_Ng "Andrew Ng")

 |  
| Social, economic, and governance  | 
  * [AI boom](https://en.wikipedia.org/wiki/AI_boom "AI boom")
  * [AI bubble](https://en.wikipedia.org/wiki/AI_bubble "AI bubble")
  * [AI slop](https://en.wikipedia.org/wiki/AI_slop "AI slop")
  * [AI anthropomorphism](https://en.wikipedia.org/wiki/AI_anthropomorphism "AI anthropomorphism")
  * [AI arms race](https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race "Artificial intelligence arms race")
  * [Chatbot psychosis](https://en.wikipedia.org/wiki/Chatbot_psychosis "Chatbot psychosis")
  * [Competition](https://en.wikipedia.org/wiki/Competition_in_artificial_intelligence "Competition in artificial intelligence")
  * [Copyright](https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright "Artificial intelligence and copyright")
  * [Deaths linked to chatbots](https://en.wikipedia.org/wiki/Deaths_linked_to_chatbots "Deaths linked to chatbots")
  * [Environmental impact](https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence "Environmental impact of artificial intelligence")
  * [Regulation](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence "Regulation of artificial intelligence")
  * [Ethics](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence "Ethics of artificial intelligence")
  * [Existential risk](https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence "Existential risk from artificial intelligence")
  * [In education](https://en.wikipedia.org/wiki/Artificial_intelligence_in_education "Artificial intelligence in education")
  * [In healthcare](https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare "Artificial intelligence in healthcare")
  * [Workplace impact](https://en.wikipedia.org/wiki/Workplace_impact_of_artificial_intelligence "Workplace impact of artificial intelligence")

 |  
| 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category:Large language models](https://en.wikipedia.org/wiki/Category:Large_language_models "Category:Large language models")

 |  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Natural_language_processing "Template:Natural language processing")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Natural_language_processing "Template talk:Natural language processing")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Natural_language_processing "Special:EditPage/Template:Natural language processing")

[Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing")  |  
| --- |  
| General terms  | 
  * [AI-complete](https://en.wikipedia.org/wiki/AI-complete "AI-complete")
  * [Bag-of-words](https://en.wikipedia.org/wiki/Bag-of-words_model "Bag-of-words model")
  * [_n_ -gram](https://en.wikipedia.org/wiki/N-gram "N-gram")
    * [Bigram](https://en.wikipedia.org/wiki/Bigram "Bigram")
    * [Trigram](https://en.wikipedia.org/wiki/Trigram "Trigram")
  * [Computational linguistics](https://en.wikipedia.org/wiki/Computational_linguistics "Computational linguistics")
  * [Natural language understanding](https://en.wikipedia.org/wiki/Natural_language_understanding "Natural language understanding")
  * [Stop words](https://en.wikipedia.org/wiki/Stop_word "Stop word")
  * [Text processing](https://en.wikipedia.org/wiki/Text_processing "Text processing")

 |  
| [Text analysis](https://en.wikipedia.org/wiki/Text_mining "Text mining")  | 
  * [Argument mining](https://en.wikipedia.org/wiki/Argument_mining "Argument mining")
  * [Collocation extraction](https://en.wikipedia.org/wiki/Collocation_extraction "Collocation extraction")
  * [Concept mining](https://en.wikipedia.org/wiki/Concept_mining "Concept mining")
  * [Coreference resolution](https://en.wikipedia.org/wiki/Coreference#Coreference_resolution "Coreference")
  * [Deep linguistic processing](https://en.wikipedia.org/wiki/Deep_linguistic_processing "Deep linguistic processing")
  * [Distant reading](https://en.wikipedia.org/wiki/Distant_reading "Distant reading")
  * [Information extraction](https://en.wikipedia.org/wiki/Information_extraction "Information extraction")
  * [Named-entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition "Named-entity recognition")
  * [Ontology learning](https://en.wikipedia.org/wiki/Ontology_learning "Ontology learning")
  * [Parsing](https://en.wikipedia.org/wiki/Parsing "Parsing")
    * [semantic](https://en.wikipedia.org/wiki/Semantic_parsing "Semantic parsing")
    * [syntactic](https://en.wikipedia.org/wiki/Syntactic_parsing_\(computational_linguistics\) "Syntactic parsing \(computational linguistics\)")
  * [Part-of-speech tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging "Part-of-speech tagging")
  * [Semantic analysis](https://en.wikipedia.org/wiki/Semantic_analysis_\(machine_learning\) "Semantic analysis \(machine learning\)")
  * [Semantic role labeling](https://en.wikipedia.org/wiki/Semantic_role_labeling "Semantic role labeling")
  * [Semantic decomposition](https://en.wikipedia.org/wiki/Semantic_decomposition_\(natural_language_processing\) "Semantic decomposition \(natural language processing\)")
  * [Semantic similarity](https://en.wikipedia.org/wiki/Semantic_similarity "Semantic similarity")
  * [Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis "Sentiment analysis")
  * [Stylometry](https://en.wikipedia.org/wiki/Stylometry "Stylometry")
    * [adversarial](https://en.wikipedia.org/wiki/Adversarial_stylometry "Adversarial stylometry")
  * [Terminology extraction](https://en.wikipedia.org/wiki/Terminology_extraction "Terminology extraction")
  * [Text mining](https://en.wikipedia.org/wiki/Text_mining "Text mining")
  * [Textual entailment](https://en.wikipedia.org/wiki/Textual_entailment "Textual entailment")
  * [Truecasing](https://en.wikipedia.org/wiki/Truecasing "Truecasing")
  * [Word-sense disambiguation](https://en.wikipedia.org/wiki/Word-sense_disambiguation "Word-sense disambiguation")
  * [Word-sense induction](https://en.wikipedia.org/wiki/Word-sense_induction "Word-sense induction")

  
 | [Text segmentation](https://en.wikipedia.org/wiki/Text_segmentation "Text segmentation")  | 
  * [Compound-term processing](https://en.wikipedia.org/wiki/Compound-term_processing "Compound-term processing")
  * [Lemmatization](https://en.wikipedia.org/wiki/Lemmatization "Lemmatization")
  * [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis "Lexical analysis")
  * [Text chunking](https://en.wikipedia.org/wiki/Shallow_parsing "Shallow parsing")
  * [Stemming](https://en.wikipedia.org/wiki/Stemming "Stemming")
  * [Sentence segmentation](https://en.wikipedia.org/wiki/Sentence_boundary_disambiguation "Sentence boundary disambiguation")
  * [Word segmentation](https://en.wikipedia.org/wiki/Word#Word_boundaries "Word")

 |  
| --- | --- |  
 |  
| [Automatic summarization](https://en.wikipedia.org/wiki/Automatic_summarization "Automatic summarization")  | 
  * [Multi-document summarization](https://en.wikipedia.org/wiki/Multi-document_summarization "Multi-document summarization")
  * [Sentence extraction](https://en.wikipedia.org/wiki/Sentence_extraction "Sentence extraction")
  * [Text simplification](https://en.wikipedia.org/wiki/Text_simplification "Text simplification")

 |  
| [Machine translation](https://en.wikipedia.org/wiki/Machine_translation "Machine translation")  | 
  * [Computer-assisted](https://en.wikipedia.org/wiki/Computer-assisted_translation "Computer-assisted translation")
  * [Example-based](https://en.wikipedia.org/wiki/Example-based_machine_translation "Example-based machine translation")
  * [Rule-based](https://en.wikipedia.org/wiki/Rule-based_machine_translation "Rule-based machine translation")
  * [Statistical](https://en.wikipedia.org/wiki/Statistical_machine_translation "Statistical machine translation")
  * [Transfer-based](https://en.wikipedia.org/wiki/Transfer-based_machine_translation "Transfer-based machine translation")
  * [Neural](https://en.wikipedia.org/wiki/Neural_machine_translation "Neural machine translation")

 |  
|  [Distributional semantics](https://en.wikipedia.org/wiki/Distributional_semantics "Distributional semantics") models  | 
  * BERT
  * [Document-term matrix](https://en.wikipedia.org/wiki/Document-term_matrix "Document-term matrix")
  * [Explicit semantic analysis](https://en.wikipedia.org/wiki/Explicit_semantic_analysis "Explicit semantic analysis")
  * [fastText](https://en.wikipedia.org/wiki/FastText "FastText")
  * [GloVe](https://en.wikipedia.org/wiki/GloVe "GloVe")
  * [Language model](https://en.wikipedia.org/wiki/Language_model "Language model")
    * [large](https://en.wikipedia.org/wiki/Large_language_model "Large language model")
    * [small](https://en.wikipedia.org/wiki/Small_language_model "Small language model")
  * [Latent semantic analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis "Latent semantic analysis")
  * [Long short-term memory](https://en.wikipedia.org/wiki/Long_short-term_memory "Long short-term memory")
  * [Seq2seq](https://en.wikipedia.org/wiki/Seq2seq "Seq2seq")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning_architecture\) "Transformer \(deep learning architecture\)")
  * [Word embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding")
  * [Word2vec](https://en.wikipedia.org/wiki/Word2vec "Word2vec")

 |  
|  [Language resources](https://en.wikipedia.org/wiki/Language_resource "Language resource"),  
datasets and corpora  |   
 | Types and  
standards  | 
  * [Corpus linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics "Corpus linguistics")
  * [Lexical resource](https://en.wikipedia.org/wiki/Lexical_resource "Lexical resource")
  * [Linguistic Linked Open Data](https://en.wikipedia.org/wiki/Linguistic_Linked_Open_Data "Linguistic Linked Open Data")
  * [Machine-readable dictionary](https://en.wikipedia.org/wiki/Machine-readable_dictionary "Machine-readable dictionary")
  * [Parallel text](https://en.wikipedia.org/wiki/Parallel_text "Parallel text")
  * [PropBank](https://en.wikipedia.org/wiki/PropBank "PropBank")
  * [Semantic network](https://en.wikipedia.org/wiki/Semantic_network "Semantic network")
  * [Simple Knowledge Organization System](https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System "Simple Knowledge Organization System")
  * [Speech corpus](https://en.wikipedia.org/wiki/Speech_corpus "Speech corpus")
  * [Text corpus](https://en.wikipedia.org/wiki/Text_corpus "Text corpus")
  * [Thesaurus (information retrieval)](https://en.wikipedia.org/wiki/Thesaurus_\(information_retrieval\) "Thesaurus \(information retrieval\)")
  * [Treebank](https://en.wikipedia.org/wiki/Treebank "Treebank")
  * [Universal Dependencies](https://en.wikipedia.org/wiki/Universal_Dependencies "Universal Dependencies")

 |  
| --- | --- |  
| Data  | 
  * [BabelNet](https://en.wikipedia.org/wiki/BabelNet "BabelNet")
  * [Bank of English](https://en.wikipedia.org/wiki/Bank_of_English "Bank of English")
  * [DBpedia](https://en.wikipedia.org/wiki/DBpedia "DBpedia")
  * [FrameNet](https://en.wikipedia.org/wiki/FrameNet "FrameNet")
  * [Google Ngram Viewer](https://en.wikipedia.org/wiki/Google_Ngram_Viewer "Google Ngram Viewer")
  * [UBY](https://en.wikipedia.org/wiki/UBY "UBY")
  * [WordNet](https://en.wikipedia.org/wiki/WordNet "WordNet")
  * [Wikidata](https://en.wikipedia.org/wiki/Wikidata "Wikidata")

 |  
 |  
| [Automatic identification  
and data capture](https://en.wikipedia.org/wiki/Automatic_identification_and_data_capture "Automatic identification and data capture")  | 
  * [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition "Speech recognition")
  * [Speech segmentation](https://en.wikipedia.org/wiki/Speech_segmentation "Speech segmentation")
  * [Speech synthesis](https://en.wikipedia.org/wiki/Speech_synthesis "Speech synthesis")
  * [Natural language generation](https://en.wikipedia.org/wiki/Natural_language_generation "Natural language generation")
  * [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition "Optical character recognition")

 |  
| [Topic model](https://en.wikipedia.org/wiki/Topic_model "Topic model")  | 
  * [Document classification](https://en.wikipedia.org/wiki/Document_classification "Document classification")
  * [Latent Dirichlet allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation "Latent Dirichlet allocation")
  * [Pachinko allocation](https://en.wikipedia.org/wiki/Pachinko_allocation "Pachinko allocation")

 |  
| [Computer-assisted  
reviewing](https://en.wikipedia.org/wiki/Computer-assisted_reviewing "Computer-assisted reviewing")  | 
  * [Automated essay scoring](https://en.wikipedia.org/wiki/Automated_essay_scoring "Automated essay scoring")
  * [Concordancer](https://en.wikipedia.org/wiki/Concordancer "Concordancer")
  * [Grammar checker](https://en.wikipedia.org/wiki/Grammar_checker "Grammar checker")
  * [Predictive text](https://en.wikipedia.org/wiki/Predictive_text "Predictive text")
  * [Pronunciation assessment](https://en.wikipedia.org/wiki/Pronunciation_assessment "Pronunciation assessment")
  * [Spell checker](https://en.wikipedia.org/wiki/Spell_checker "Spell checker")

 |  
| [Natural language  
user interface](https://en.wikipedia.org/wiki/Natural-language_user_interface "Natural-language user interface")  | 
  * [Chatbot](https://en.wikipedia.org/wiki/Chatbot "Chatbot")
  * [Interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction "Interactive fiction")
  * [Question answering](https://en.wikipedia.org/wiki/Question_answering "Question answering")
  * [Virtual assistant](https://en.wikipedia.org/wiki/Virtual_assistant "Virtual assistant")
  * [Voice user interface](https://en.wikipedia.org/wiki/Voice_user_interface "Voice user interface")

 |  
| Related  | 
  * [Formal semantics](https://en.wikipedia.org/wiki/Formal_semantics_\(natural_language\) "Formal semantics \(natural language\)")
  * [Gensim](https://en.wikipedia.org/wiki/Gensim "Gensim")
  * [Hallucination](https://en.wikipedia.org/wiki/Hallucination_\(artificial_intelligence\) "Hallucination \(artificial intelligence\)")
  * [Natural Language Toolkit](https://en.wikipedia.org/wiki/Natural_Language_Toolkit "Natural Language Toolkit")
  * [spaCy](https://en.wikipedia.org/wiki/SpaCy "SpaCy")

 |  
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
  * [RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")
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
Retrieved from "[https://en.wikipedia.org/w/index.php?title=BERT_(language_model)&oldid=1356209197](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&oldid=1356209197)"
[Categories](https://en.wikipedia.org/wiki/Help:Category "Help:Category"): 
  * [Google software](https://en.wikipedia.org/wiki/Category:Google_software "Category:Google software")
  * [Large language models](https://en.wikipedia.org/wiki/Category:Large_language_models "Category:Large language models")
  * [2018 software](https://en.wikipedia.org/wiki/Category:2018_software "Category:2018 software")
  * [2018 in artificial intelligence](https://en.wikipedia.org/wiki/Category:2018_in_artificial_intelligence "Category:2018 in artificial intelligence")


Hidden categories: 
  * [Articles with short description](https://en.wikipedia.org/wiki/Category:Articles_with_short_description "Category:Articles with short description")
  * [Short description is different from Wikidata](https://en.wikipedia.org/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
  * [Use mdy dates from November 2023](https://en.wikipedia.org/wiki/Category:Use_mdy_dates_from_November_2023 "Category:Use mdy dates from November 2023")
  * [Use American English from November 2023](https://en.wikipedia.org/wiki/Category:Use_American_English_from_November_2023 "Category:Use American English from November 2023")
  * [All Wikipedia articles written in American English](https://en.wikipedia.org/wiki/Category:All_Wikipedia_articles_written_in_American_English "Category:All Wikipedia articles written in American English")
  * [Articles containing potentially dated statements from 2020](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2020 "Category:Articles containing potentially dated statements from 2020")
  * [All articles containing potentially dated statements](https://en.wikipedia.org/wiki/Category:All_articles_containing_potentially_dated_statements "Category:All articles containing potentially dated statements")


  * This page was last edited on 26 May 2026, at 10:10 (UTC).
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
  * [Mobile view](https://en.wikipedia.org/w/index.php?title=BERT_\(language_model\)&mobileaction=toggle_view_mobile)


  * [![Wikimedia Foundation](https://en.wikipedia.org/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
  * [![Powered by MediaWiki](https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)


Search
Search
Toggle the table of contents
BERT (language model)
[](https://en.wikipedia.org/wiki/BERT_\(language_model\)) [](https://en.wikipedia.org/wiki/BERT_\(language_model\)) [](https://en.wikipedia.org/wiki/BERT_\(language_model\)) [](https://en.wikipedia.org/wiki/BERT_\(language_model\)) [](https://en.wikipedia.org/wiki/BERT_\(language_model\)) [](https://en.wikipedia.org/wiki/BERT_\(language_model\)) [](https://en.wikipedia.org/wiki/BERT_\(language_model\))
22 languages [Add topic ](https://en.wikipedia.org/wiki/BERT_\(language_model\))
  *[v]: View this template
  *[t]: Discuss this template
  *[e]: Edit this template
