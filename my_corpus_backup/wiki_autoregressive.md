[Jump to content](https://en.wikipedia.org/wiki/Autoregressive_model#bodyContent)
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
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Autoregressive+model "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Autoregressive+model "You're encouraged to log in; however, it's not mandatory. \[o\]")


Personal tools
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Autoregressive+model "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Autoregressive+model "You're encouraged to log in; however, it's not mandatory. \[o\]")


## Contents
move to sidebar hide
  * [ (Top) ](https://en.wikipedia.org/wiki/Autoregressive_model)
  * [ 1 Definition ](https://en.wikipedia.org/wiki/Autoregressive_model#Definition)
  * [ 2 Intertemporal effect of shocks ](https://en.wikipedia.org/wiki/Autoregressive_model#Intertemporal_effect_of_shocks)
  * [ 3 Characteristic polynomial ](https://en.wikipedia.org/wiki/Autoregressive_model#Characteristic_polynomial)
  * [ 4 Graphs of AR(_p_) processes ](https://en.wikipedia.org/wiki/Autoregressive_model#Graphs_of_AR\(p\)_processes)
  * [ 5 Example: An AR(1) process ](https://en.wikipedia.org/wiki/Autoregressive_model#Example:_An_AR\(1\)_process) Toggle Example: An AR(1) process subsection
    * [ 5.1 Explicit mean/difference form of AR(1) process ](https://en.wikipedia.org/wiki/Autoregressive_model#Explicit_mean/difference_form_of_AR\(1\)_process)
  * [ 6 Choosing the maximum lag ](https://en.wikipedia.org/wiki/Autoregressive_model#Choosing_the_maximum_lag)
  * [ 7 Calculation of the AR parameters ](https://en.wikipedia.org/wiki/Autoregressive_model#Calculation_of_the_AR_parameters) Toggle Calculation of the AR parameters subsection
    * [ 7.1 Yule–Walker equations ](https://en.wikipedia.org/wiki/Autoregressive_model#Yule%E2%80%93Walker_equations)
    * [ 7.2 Estimation of AR parameters ](https://en.wikipedia.org/wiki/Autoregressive_model#Estimation_of_AR_parameters)
  * [ 8 Spectrum ](https://en.wikipedia.org/wiki/Autoregressive_model#Spectrum) Toggle Spectrum subsection
    * [ 8.1 AR(0) ](https://en.wikipedia.org/wiki/Autoregressive_model#AR\(0\))
    * [ 8.2 AR(1) ](https://en.wikipedia.org/wiki/Autoregressive_model#AR\(1\))
    * [ 8.3 AR(2) ](https://en.wikipedia.org/wiki/Autoregressive_model#AR\(2\))
  * [ 9 Implementations in statistics packages ](https://en.wikipedia.org/wiki/Autoregressive_model#Implementations_in_statistics_packages)
  * [ 10 Impulse response ](https://en.wikipedia.org/wiki/Autoregressive_model#Impulse_response)
  * [ 11 _n_ -step-ahead forecasting ](https://en.wikipedia.org/wiki/Autoregressive_model#n-step-ahead_forecasting)
  * [ 12 See also ](https://en.wikipedia.org/wiki/Autoregressive_model#See_also)
  * [ 13 Notes ](https://en.wikipedia.org/wiki/Autoregressive_model#Notes)
  * [ 14 References ](https://en.wikipedia.org/wiki/Autoregressive_model#References)
  * [ 15 External links ](https://en.wikipedia.org/wiki/Autoregressive_model#External_links)


Toggle the table of contents
# Autoregressive model
20 languages
  * [Català](https://ca.wikipedia.org/wiki/Model_autoregressiu "Model autoregressiu – Catalan")
  * [Español](https://es.wikipedia.org/wiki/Modelo_autorregresivo "Modelo autorregresivo – Spanish")
  * [فارسی](https://fa.wikipedia.org/wiki/%D9%85%D8%AF%D9%84_%D8%AE%D9%88%D8%AF%D9%87%D9%85%D8%A8%D8%B3%D8%AA%D9%87 "مدل خودهمبسته – Persian")
  * [Français](https://fr.wikipedia.org/wiki/Processus_autor%C3%A9gressif "Processus autorégressif – French")
  * [עברית](https://he.wikipedia.org/wiki/%D7%9E%D7%95%D7%93%D7%9C_%D7%90%D7%95%D7%98%D7%95-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%91%D7%99 "מודל אוטו-רגרסיבי – Hebrew")
  * [Italiano](https://it.wikipedia.org/wiki/Modello_autoregressivo "Modello autoregressivo – Italian")
  * [日本語](https://ja.wikipedia.org/wiki/%E8%87%AA%E5%B7%B1%E5%9B%9E%E5%B8%B0%E3%83%A2%E3%83%87%E3%83%AB "自己回帰モデル – Japanese")
  * [한국어](https://ko.wikipedia.org/wiki/%EC%9E%90%EA%B8%B0%ED%9A%8C%EA%B7%80%EB%AA%A8%ED%98%95 "자기회귀모형 – Korean")
  * [Македонски](https://mk.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D0%B8%D0%B2%D0%B5%D0%BD_%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81 "Авторегресивен процес – Macedonian")
  * [Nederlands](https://nl.wikipedia.org/wiki/Autoregressief_model "Autoregressief model – Dutch")
  * [Polski](https://pl.wikipedia.org/wiki/Model_AR "Model AR – Polish")
  * [Português](https://pt.wikipedia.org/wiki/Modelo_autorregressivo "Modelo autorregressivo – Portuguese")
  * [Русский](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C "Авторегрессионная модель – Russian")
  * [Simple English](https://simple.wikipedia.org/wiki/Autoregressive_model "Autoregressive model – Simple English")
  * [Svenska](https://sv.wikipedia.org/wiki/Autoregressiv "Autoregressiv – Swedish")
  * [Türkçe](https://tr.wikipedia.org/wiki/%C3%96zba%C4%9Flan%C4%B1ml%C4%B1_model "Özbağlanımlı model – Turkish")
  * [Українська](https://uk.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%96%D0%B9%D0%BD%D0%B0_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C "Авторегресійна модель – Ukrainian")
  * [閩南語 / Bân-lâm-gí](https://zh-min-nan.wikipedia.org/wiki/Ch%C5%AB-k%C3%AD_h%C3%B4e-kui_b%C3%B4%CD%98-h%C3%AAng "Chū-kí hôe-kui bô͘-hêng – Minnan")
  * [粵語](https://zh-yue.wikipedia.org/wiki/%E8%87%AA%E8%BF%B4%E6%AD%B8%E6%A8%A1%E5%9E%8B "自迴歸模型 – Cantonese")
  * [中文](https://zh.wikipedia.org/wiki/%E8%87%AA%E6%88%91%E8%BF%B4%E6%AD%B8%E6%A8%A1%E5%9E%8B "自我迴歸模型 – Chinese")


[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q2202883#sitelinks-wikipedia "Edit interlanguage links")
  * [Article](https://en.wikipedia.org/wiki/Autoregressive_model "View the content page \[c\]")
  * [Talk](https://en.wikipedia.org/wiki/Talk:Autoregressive_model "Discuss improvements to the content page \[t\]")


English
  * [Read](https://en.wikipedia.org/wiki/Autoregressive_model)
  * [Edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=history "Past revisions of this page \[h\]")


Tools
Tools
move to sidebar hide
Actions 
  * [Read](https://en.wikipedia.org/wiki/Autoregressive_model)
  * [Edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=history)


General 
  * [What links here](https://en.wikipedia.org/wiki/Special:WhatLinksHere/Autoregressive_model "List of all English Wikipedia pages containing links to this page \[j\]")
  * [Related changes](https://en.wikipedia.org/wiki/Special:RecentChangesLinked/Autoregressive_model "Recent changes in pages linked from this page \[k\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files \[u\]")
  * [Permanent link](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&oldid=1358105099 "Permanent link to this revision of this page")
  * [Page information](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=info "More information about this page")
  * [Cite this page](https://en.wikipedia.org/w/index.php?title=Special:CiteThisPage&page=Autoregressive_model&id=1358105099&wpFormIdentifier=titleform "Information on how to cite this page")
  * [Get shortened URL](https://en.wikipedia.org/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAutoregressive_model)


Print/export 
  * [Download as PDF](https://en.wikipedia.org/w/index.php?title=Special:DownloadAsPdf&page=Autoregressive_model&action=show-download-screen "Download this page as a PDF file")
  * [Printable version](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&printable=yes "Printable version of this page \[p\]")


In other projects 
  * [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q2202883 "Structured data on this page hosted by Wikidata \[g\]")


Appearance
move to sidebar hide
From Wikipedia, the free encyclopedia
Representation of a type of random process  
| ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Text_document_with_red_question_mark.svg/40px-Text_document_with_red_question_mark.svg.png)  | This article includes a list of [general references](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#General_references "Wikipedia:Citing sources"), but **it lacks sufficient corresponding[inline citations](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#Inline_citations "Wikipedia:Citing sources")**. Please help to [improve](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Reliability "Wikipedia:WikiProject Reliability") this article by [introducing](https://en.wikipedia.org/wiki/Wikipedia:When_to_cite "Wikipedia:When to cite") more precise citations. _( March 2011)__([Learn how and when to remove this message](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  |  
| --- | --- |  
In [statistics](https://en.wikipedia.org/wiki/Statistics "Statistics"), an **autoregressive** (**AR**) **model** is a [modelled](https://en.wikipedia.org/wiki/Mathematical_model "Mathematical model") representation of a type of [random process](https://en.wikipedia.org/wiki/Stochastic_process "Stochastic process"). It can be used to describe [time-varying processes](https://en.wikipedia.org/wiki/Time_series "Time series") from many natural and artificial sources. The model specifies output variables that are dependent [linearly](https://en.wikipedia.org/wiki/Linear_relation "Linear relation") on their own previous values on a [stochastic](https://en.wikipedia.org/wiki/Stochastic "Stochastic") basis. The model is in the form of a stochastic [difference equation](https://en.wikipedia.org/wiki/Difference_equation "Difference equation") (or [recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation "Recurrence relation")) which should not be confused with a [differential equation](https://en.wikipedia.org/wiki/Differential_equation "Differential equation"). Together with the [moving-average (MA) model](https://en.wikipedia.org/wiki/Moving-average_model "Moving-average model"), it is a special case and key component of the more general [autoregressive–moving-average](https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model "Autoregressive–moving-average model") (ARMA) and [autoregressive integrated moving average](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average "Autoregressive integrated moving average") (ARIMA) models of time series, which have a more complicated stochastic structure; it is also a special case of the vector autoregressive model (VAR), which consists of a system of more than one interlocking stochastic difference equation in more than one evolving random variable. 
Another important extension is the time-varying autoregressive (TVAR) model, where the autoregressive coefficients are allowed to change over time to model evolving or non-stationary processes. TVAR models are widely applied in cases where the underlying dynamics of the system are not constant, such as in sensors time series modelling,[[1]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-1)[[2]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-2) [climate science](https://en.wikipedia.org/wiki/Climatology "Climatology"),[[3]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-3) economics and finance (as [econometrics](https://en.wikipedia.org/wiki/Econometrics "Econometrics")),[[4]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-4)[[5]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-5) [signal processing](https://en.wikipedia.org/wiki/Signal_processing "Signal processing"),[[6]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-6) [telecommunications](https://en.wikipedia.org/wiki/Telecommunications "Telecommunications"),[[7]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-7) [radar](https://en.wikipedia.org/wiki/Radar "Radar") systems,[[8]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-8) and [biological](https://en.wikipedia.org/wiki/Biology "Biology") signals.[[9]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-9)
Unlike the moving-average (MA) model, the autoregressive model is not always stationary; non-stationarity can arise either due to the presence of a [unit root](https://en.wikipedia.org/wiki/Unit_root "Unit root") or due to time-varying model parameters, as in time-varying autoregressive models. 
[Large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") are called autoregressive, but they are not a classical autoregressive model in this sense because they are not linear. 
## Definition
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=1 "Edit section: Definition")]
The notation  A R ( p ) {\displaystyle AR(p)} ![{\\displaystyle AR\(p\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/656b65718fc07fb84c0d8186c6e43ce76723427b) indicates an autoregressive model of order _p_. The AR(_p_) model is defined as       X t = ∑ i = 1 p φ i X t − i + ε t {\displaystyle X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t-i}+\varepsilon _{t}} ![{\\displaystyle X_{t}=\\sum _{i=1}^{p}\\varphi _{i}X_{t-i}+\\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0bec4e5efbcc95f1fb648c8c03686c4b3843b04)
where  φ 1 , … , φ p {\displaystyle \varphi _{1},\ldots ,\varphi _{p}} ![{\\displaystyle \\varphi _{1},\\ldots ,\\varphi _{p}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d4fdc81c8ea00ebabdeee779385a8e22e3c2b385) are the _parameters_ of the model, and  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) is [white noise](https://en.wikipedia.org/wiki/White_noise "White noise").[[10]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-10)[[11]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-11) This can be equivalently written using the [backshift operator](https://en.wikipedia.org/wiki/Backshift_operator "Backshift operator") _B_ as       X t = ∑ i = 1 p φ i B i X t + ε t {\displaystyle X_{t}=\sum _{i=1}^{p}\varphi _{i}B^{i}X_{t}+\varepsilon _{t}} ![{\\displaystyle X_{t}=\\sum _{i=1}^{p}\\varphi _{i}B^{i}X_{t}+\\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f1df0884c60da1ead623e7b11b99fb0945441f5a)
so that, moving the summation term to the left side and using [polynomial notation](https://en.wikipedia.org/wiki/Polynomial_notation "Polynomial notation"), we have       φ ( B ) X t = ε t {\displaystyle \varphi (B)X_{t}=\varepsilon _{t}} ![{\\displaystyle \\varphi \(B\)X_{t}=\\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3eaed4098dda56f9ccc15ec24acb438642173a9c)
An autoregressive model can thus be viewed as the output of an all-[pole](https://en.wikipedia.org/wiki/Pole_\(complex_analysis\) "Pole \(complex analysis\)") [infinite impulse response](https://en.wikipedia.org/wiki/Infinite_impulse_response "Infinite impulse response") filter whose input is white noise. 
Some parameter constraints are necessary for the model to remain [weak-sense stationary](https://en.wikipedia.org/wiki/Stationary_process#Weak_or_wide-sense_stationarity "Stationary process"). For example, processes in the AR(1) model with  | φ 1 | ≥ 1 {\displaystyle |\varphi _{1}|\geq 1} ![{\\displaystyle |\\varphi _{1}|\\geq 1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5feb9de2fe8907d308f9eaaab3ff940d54b8fbf9) are not stationary. More generally, for an AR(_p_) model to be weak-sense stationary, the roots of the polynomial  Φ ( z ) := 1 − ∑ i = 1 p φ i z i {\displaystyle \Phi (z):=\textstyle 1-\sum _{i=1}^{p}\varphi _{i}z^{i}} ![{\\displaystyle \\Phi \(z\):=\\textstyle 1-\\sum _{i=1}^{p}\\varphi _{i}z^{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/28c983acd51d75155b677b0237020037000c501c) must lie outside the [unit circle](https://en.wikipedia.org/wiki/Unit_circle "Unit circle"), i.e., each (complex) root  z i {\displaystyle z_{i}} ![{\\displaystyle z_{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5c6e920bac39ad09fff4efef16254595091a1025) must satisfy  | z i | > 1 {\displaystyle |z_{i}|>1} ![{\\displaystyle |z_{i}|>1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ff75c25f97e572744f6a3c93410506ce35cd1d1e) (see pages 89,92 [[12]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-12)). 
## Intertemporal effect of shocks
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=2 "Edit section: Intertemporal effect of shocks")]
In an AR process, a one-time shock affects values of the evolving variable infinitely far into the future. For example, consider the AR(1) model  X t = φ 1 X t − 1 + ε t {\displaystyle X_{t}=\varphi _{1}X_{t-1}+\varepsilon _{t}} ![{\\displaystyle X_{t}=\\varphi _{1}X_{t-1}+\\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/62e702d3e4a52abad2784f06fb45d2c530702773). A non-zero value for  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) at say time _t_ =1 affects  X 1 {\displaystyle X_{1}} ![{\\displaystyle X_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f70b2694445a5901b24338a2e7a7e58f02a72a32) by the amount  ε 1 {\displaystyle \varepsilon _{1}} ![{\\displaystyle \\varepsilon _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9e900f9bee793f99d10877ef108da074cbca60ce). Then by the AR equation for  X 2 {\displaystyle X_{2}} ![{\\displaystyle X_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2ad47c14b8a092f182512e76c96638aea6e3bea1) in terms of  X 1 {\displaystyle X_{1}} ![{\\displaystyle X_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f70b2694445a5901b24338a2e7a7e58f02a72a32), this affects  X 2 {\displaystyle X_{2}} ![{\\displaystyle X_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2ad47c14b8a092f182512e76c96638aea6e3bea1) by the amount  φ 1 ε 1 {\displaystyle \varphi _{1}\varepsilon _{1}} ![{\\displaystyle \\varphi _{1}\\varepsilon _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e6771fe396d6eec7394996b530cb986db71feea4). Then by the AR equation for  X 3 {\displaystyle X_{3}} ![{\\displaystyle X_{3}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/14f17eb6a51e16ea92736c904a92d8a78e73a598) in terms of  X 2 {\displaystyle X_{2}} ![{\\displaystyle X_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2ad47c14b8a092f182512e76c96638aea6e3bea1), this affects  X 3 {\displaystyle X_{3}} ![{\\displaystyle X_{3}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/14f17eb6a51e16ea92736c904a92d8a78e73a598) by the amount  φ 1 2 ε 1 {\displaystyle \varphi _{1}^{2}\varepsilon _{1}} ![{\\displaystyle \\varphi _{1}^{2}\\varepsilon _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e47bea8b4509e8572bfbd52a6989c11ab084d724). Continuing this process shows that the effect of  ε 1 {\displaystyle \varepsilon _{1}} ![{\\displaystyle \\varepsilon _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9e900f9bee793f99d10877ef108da074cbca60ce) never ends, although if the process is [stationary](https://en.wikipedia.org/wiki/Stationary_process "Stationary process") then the effect diminishes toward zero in the limit. 
Because each shock affects _X_ values infinitely far into the future from when they occur, any given value _X_ _t_ is affected by shocks occurring infinitely far into the past. This can also be seen by rewriting the autoregression       φ ( B ) X t = ε t {\displaystyle \varphi (B)X_{t}=\varepsilon _{t}\,} ![{\\displaystyle \\varphi \(B\)X_{t}=\\varepsilon _{t}\\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a67aeec25585797e8e95875874e121eb19523a5a)
(where the constant term has been suppressed by assuming that the variable has been measured as deviations from its mean) as       X t = 1 φ ( B ) ε t . {\displaystyle X_{t}={\frac {1}{\varphi (B)}}\varepsilon _{t}\,.} ![{\\displaystyle X_{t}={\\frac {1}{\\varphi \(B\)}}\\varepsilon _{t}\\,.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/008ccafdb5a2964901954a28ab45251c29d72da4)
When the [polynomial division](https://en.wikipedia.org/wiki/Polynomial_long_division "Polynomial long division") on the right side is carried out, the polynomial in the backshift operator applied to  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) has an infinite order—that is, an infinite number of lagged values of  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) appear on the right side of the equation. 
## Characteristic polynomial
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=3 "Edit section: Characteristic polynomial")]
The [autocorrelation function](https://en.wikipedia.org/wiki/Autocorrelation_function "Autocorrelation function") of an AR(_p_) process can be expressed as [_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]      ρ ( τ ) = ∑ k = 1 p a k y k − | τ | , {\displaystyle \rho (\tau )=\sum _{k=1}^{p}a_{k}y_{k}^{-|\tau |},} ![{\\displaystyle \\rho \(\\tau \)=\\sum _{k=1}^{p}a_{k}y_{k}^{-|\\tau |},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/979241068653d54f8ce728e1d16e45df688a69fc)
where  y k {\displaystyle y_{k}} ![{\\displaystyle y_{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4b2ab0248723a410cc2c67ce06ad5c043dcbb933) are the roots of the polynomial       φ ( B ) = 1 − ∑ k = 1 p φ k B k {\displaystyle \varphi (B)=1-\sum _{k=1}^{p}\varphi _{k}B^{k}} ![{\\displaystyle \\varphi \(B\)=1-\\sum _{k=1}^{p}\\varphi _{k}B^{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e2301c2da799c65cae395a795e2eabd190aa98f3)
where _B_ is the [backshift operator](https://en.wikipedia.org/wiki/Backshift_operator "Backshift operator"), where  φ ( ⋅ ) {\displaystyle \varphi (\cdot )} ![{\\displaystyle \\varphi \(\\cdot \)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/20f699669bedbc11c472c37d63f2ca9337be4649) is the function defining the autoregression, and where  φ k {\displaystyle \varphi _{k}} ![{\\displaystyle \\varphi _{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/dad86b92f0c76d343e12c4a90b368834329bd5d6) are the coefficients in the autoregression. The formula is valid only if all the roots have multiplicity 1.[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]
The autocorrelation function of an AR(_p_) process is a sum of decaying exponentials. 
  * Each real root contributes a component to the autocorrelation function that decays exponentially.
  * Similarly, each pair of [complex conjugate](https://en.wikipedia.org/wiki/Complex_conjugate "Complex conjugate") roots contributes an exponentially damped oscillation.


##  _p_) processes
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=4 "Edit section: Graphs of AR\(p\) processes")]
[!["Figure has 5 plots of AR processes. AR\(0\) and AR\(0.3\) are white noise or look like white noise. AR\(0.9\) has some large scale oscillating structure."](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/ArTimeSeries.svg/250px-ArTimeSeries.svg.png)](https://en.wikipedia.org/wiki/File:ArTimeSeries.svg)AR(0); AR(1) with AR parameter 0.3; AR(1) with AR parameter 0.9; AR(2) with AR parameters 0.3 and 0.3; and AR(2) with AR parameters 0.9 and −0.8
The simplest AR process is AR(0), which has no dependence between the terms. Only the error/innovation/noise term contributes to the output of the process, so in the figure, AR(0) corresponds to white noise. 
For an AR(1) process with a positive  φ {\displaystyle \varphi } ![{\\displaystyle \\varphi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/33ee699558d09cf9d653f6351f9fda0b2f4aaa3e), only the previous term in the process and the noise term contribute to the output. If  φ {\displaystyle \varphi } ![{\\displaystyle \\varphi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/33ee699558d09cf9d653f6351f9fda0b2f4aaa3e) is close to 0, then the process still looks like white noise, but as  φ {\displaystyle \varphi } ![{\\displaystyle \\varphi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/33ee699558d09cf9d653f6351f9fda0b2f4aaa3e) approaches 1, the output gets a larger contribution from the previous term relative to the noise. This results in a "smoothing" or integration of the output, similar to a [low pass filter](https://en.wikipedia.org/wiki/Low_pass_filter "Low pass filter"). 
For an AR(2) process, the previous two terms and the noise term contribute to the output. If both  φ 1 {\displaystyle \varphi _{1}} ![{\\displaystyle \\varphi _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d7daf493c8f6ef669c04c7b9715532fc35d12d60) and  φ 2 {\displaystyle \varphi _{2}} ![{\\displaystyle \\varphi _{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c08631714273b6c8edaa9573ef3d8c548314a930) are positive, the output will resemble a low pass filter, with the high frequency part of the noise decreased. If  φ 1 {\displaystyle \varphi _{1}} ![{\\displaystyle \\varphi _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d7daf493c8f6ef669c04c7b9715532fc35d12d60) is positive while  φ 2 {\displaystyle \varphi _{2}} ![{\\displaystyle \\varphi _{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c08631714273b6c8edaa9573ef3d8c548314a930) is negative, then the process favors changes in sign between terms of the process. The output oscillates. This can be linked to edge detection or detection of change in direction. 
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=5 "Edit section: Example: An AR\(1\) process")]
An AR(1) process is given by: X t = φ X t − 1 + ε t {\displaystyle X_{t}=\varphi X_{t-1}+\varepsilon _{t}\,} ![{\\displaystyle X_{t}=\\varphi X_{t-1}+\\varepsilon _{t}\\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/19e708edb6d9fe5b8458db61d47b515a6b1e1eb3)where  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) is a white noise process with zero mean and constant variance  σ ε 2 {\displaystyle \sigma _{\varepsilon }^{2}} ![{\\displaystyle \\sigma _{\\varepsilon }^{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/eec379b86e73255492d3266c76f6e17acfdfabd1). (Note: The subscript on  φ 1 {\displaystyle \varphi _{1}} ![{\\displaystyle \\varphi _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d7daf493c8f6ef669c04c7b9715532fc35d12d60) has been dropped.) The process is [weak-sense stationary](https://en.wikipedia.org/wiki/Stationary_process#Weak_or_wide-sense_stationarity "Stationary process") if  | φ | < 1 {\displaystyle |\varphi |<1} ![{\\displaystyle |\\varphi |<1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ac88cf3e11f7577b756abedbee667cce5069563) since it is obtained as the output of a stable filter whose input is white noise. (If  φ = 1 {\displaystyle \varphi =1} ![{\\displaystyle \\varphi =1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a4d2b07a5e6f6058e04da966ccdc8506fe8ffeb2) then the variance of  X t {\displaystyle X_{t}} ![{\\displaystyle X_{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82120d04dfb3cbadc4912951dd12b5568c9cd8f3) depends on time lag _t_ , so that the variance of the series diverges to infinity as _t_ goes to infinity, and is therefore not weak-sense stationary.) Assuming  | φ | < 1 {\displaystyle |\varphi |<1} ![{\\displaystyle |\\varphi |<1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ac88cf3e11f7577b756abedbee667cce5069563), the mean  E ⁡ ( X t ) {\displaystyle \operatorname {E} (X_{t})} ![{\\displaystyle \\operatorname {E} \(X_{t}\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/be42d3e2b3cfe283a64cf222c06972633e8ded66) is identical for all values of _t_ by definition of weak sense stationarity. If the mean is denoted by  μ {\displaystyle \mu } ![{\\displaystyle \\mu }](https://wikimedia.org/api/rest_v1/media/math/render/svg/9fd47b2a39f7a7856952afec1f1db72c67af6161), it follows from E ⁡ ( X t ) = φ E ⁡ ( X t − 1 ) + E ⁡ ( ε t ) , {\displaystyle \operatorname {E} (X_{t})=\varphi \operatorname {E} (X_{t-1})+\operatorname {E} (\varepsilon _{t}),} ![{\\displaystyle \\operatorname {E} \(X_{t}\)=\\varphi \\operatorname {E} \(X_{t-1}\)+\\operatorname {E} \(\\varepsilon _{t}\),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0f51ad045dd8fbc8035f7ec65a3072550977b6e9)that μ = φ μ + 0 , {\displaystyle \mu =\varphi \mu +0,} ![{\\displaystyle \\mu =\\varphi \\mu +0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ce40dfe86cd5d47a1773eed30899000d9d46bb4e)and hence       μ = 0. {\displaystyle \mu =0.} ![{\\displaystyle \\mu =0.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6c1fbd9b60e51f99639d432b9b86c1f1f486e1b2)
The [variance](https://en.wikipedia.org/wiki/Variance "Variance") is       var ( X t ) = E ⁡ ( X t 2 ) − μ 2 = σ ε 2 1 − φ 2 , {\displaystyle {\textrm {var}}(X_{t})=\operatorname {E} (X_{t}^{2})-\mu ^{2}={\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}},} ![{\\displaystyle {\\textrm {var}}\(X_{t}\)=\\operatorname {E} \(X_{t}^{2}\)-\\mu ^{2}={\\frac {\\sigma _{\\varepsilon }^{2}}{1-\\varphi ^{2}}},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f1742b6092c63b09414e86c9e208b2da49c8dcf)
where  σ ε {\displaystyle \sigma _{\varepsilon }} ![{\\displaystyle \\sigma _{\\varepsilon }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/04852f481494a445c9f5b9082df1ead002c098a2) is the standard deviation of  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a). This can be shown by noting that       var ( X t ) = φ 2 var ( X t − 1 ) + σ ε 2 , {\displaystyle {\textrm {var}}(X_{t})=\varphi ^{2}{\textrm {var}}(X_{t-1})+\sigma _{\varepsilon }^{2},} ![{\\displaystyle {\\textrm {var}}\(X_{t}\)=\\varphi ^{2}{\\textrm {var}}\(X_{t-1}\)+\\sigma _{\\varepsilon }^{2},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c5594a5bf1cd9c13fb15eb23763328c684b41778)
and then by noticing that the quantity above is a stable fixed point of this relation. 
The [autocovariance](https://en.wikipedia.org/wiki/Autocovariance "Autocovariance") is given by       B n = E ⁡ ( X t + n X t ) − μ 2 = σ ε 2 1 − φ 2 φ | n | . {\displaystyle B_{n}=\operatorname {E} (X_{t+n}X_{t})-\mu ^{2}={\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}}\,\,\varphi ^{|n|}.} ![{\\displaystyle B_{n}=\\operatorname {E} \(X_{t+n}X_{t}\)-\\mu ^{2}={\\frac {\\sigma _{\\varepsilon }^{2}}{1-\\varphi ^{2}}}\\,\\,\\varphi ^{|n|}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8437c88291c59fdbb8055f7630becfb993b1fb17)
It can be seen that the autocovariance function decays with a decay time (also called [time constant](https://en.wikipedia.org/wiki/Time_constant "Time constant")) of  τ = 1 / ( 1 − φ ) {\displaystyle \tau =1/(1-\varphi )} ![{\\displaystyle \\tau =1/\(1-\\varphi \)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/85fb1ec990c3aae74a04441e046c7689f9180342).[[13]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-13)
The [spectral density](https://en.wikipedia.org/wiki/Spectral_density "Spectral density") function is the [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform "Fourier transform") of the autocovariance function. In discrete terms this will be the discrete-time Fourier transform:       Φ ( ω ) = 1 2 π ∑ n = − ∞ ∞ B n e − i ω n = 1 2 π ( σ ε 2 1 + φ 2 − 2 φ cos ⁡ ( ω ) ) . {\displaystyle \Phi (\omega )={\frac {1}{\sqrt {2\pi }}}\,\sum _{n=-\infty }^{\infty }B_{n}e^{-i\omega n}={\frac {1}{\sqrt {2\pi }}}\,\left({\frac {\sigma _{\varepsilon }^{2}}{1+\varphi ^{2}-2\varphi \cos(\omega )}}\right).} ![{\\displaystyle \\Phi \(\\omega \)={\\frac {1}{\\sqrt {2\\pi }}}\\,\\sum _{n=-\\infty }^{\\infty }B_{n}e^{-i\\omega n}={\\frac {1}{\\sqrt {2\\pi }}}\\,\\left\({\\frac {\\sigma _{\\varepsilon }^{2}}{1+\\varphi ^{2}-2\\varphi \\cos\(\\omega \)}}\\right\).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7fd707a70fc78fabba4b103d6099d2a75f109d02)
This expression is periodic due to the discrete nature of the  X j {\displaystyle X_{j}} ![{\\displaystyle X_{j}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ca3cb1ef7c9f25e85e1957e4eb58a72fa16a0066), which is manifested as the cosine term in the denominator. If we assume that the sampling time ( Δ t = 1 {\displaystyle \Delta t=1} ![{\\displaystyle \\Delta t=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/26978f1c5f3ac3161ce7635cbde2a207c7519aab)) is much smaller than the decay time ( τ {\displaystyle \tau } ![{\\displaystyle \\tau }](https://wikimedia.org/api/rest_v1/media/math/render/svg/38a7dcde9730ef0853809fefc18d88771f95206c)), then we can use a continuum approximation to  B n {\displaystyle B_{n}} ![{\\displaystyle B_{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/2f568bf6d34e97b9fdda0dc7e276d6c4501d2045):       B ( t ) ≈ σ ε 2 1 − φ 2 φ | t | {\displaystyle B(t)\approx {\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}}\,\,\varphi ^{|t|}} ![{\\displaystyle B\(t\)\\approx {\\frac {\\sigma _{\\varepsilon }^{2}}{1-\\varphi ^{2}}}\\,\\,\\varphi ^{|t|}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/23ab1061089249aaff9c9522ab7ba1da4296f38b)
which yields a [Lorentzian profile](https://en.wikipedia.org/wiki/Cauchy_distribution "Cauchy distribution") for the spectral density:       Φ ( ω ) = 1 2 π σ ε 2 1 − φ 2 γ π ( γ 2 + ω 2 ) {\displaystyle \Phi (\omega )={\frac {1}{\sqrt {2\pi }}}\,{\frac {\sigma _{\varepsilon }^{2}}{1-\varphi ^{2}}}\,{\frac {\gamma }{\pi (\gamma ^{2}+\omega ^{2})}}} ![{\\displaystyle \\Phi \(\\omega \)={\\frac {1}{\\sqrt {2\\pi }}}\\,{\\frac {\\sigma _{\\varepsilon }^{2}}{1-\\varphi ^{2}}}\\,{\\frac {\\gamma }{\\pi \(\\gamma ^{2}+\\omega ^{2}\)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/09c4d8d2e045f649f287fc359418e5e65e69f042)
where  γ = 1 / τ {\displaystyle \gamma =1/\tau } ![{\\displaystyle \\gamma =1/\\tau }](https://wikimedia.org/api/rest_v1/media/math/render/svg/64537ae1c00fe728d4fc64b69a72daec33b8e99c) is the angular frequency associated with the decay time  τ {\displaystyle \tau } ![{\\displaystyle \\tau }](https://wikimedia.org/api/rest_v1/media/math/render/svg/38a7dcde9730ef0853809fefc18d88771f95206c). 
An alternative expression for  X t {\displaystyle X_{t}} ![{\\displaystyle X_{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82120d04dfb3cbadc4912951dd12b5568c9cd8f3) can be derived by first substituting  φ X t − 2 + ε t − 1 {\displaystyle \varphi X_{t-2}+\varepsilon _{t-1}} ![{\\displaystyle \\varphi X_{t-2}+\\varepsilon _{t-1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0817a0d3b28f992b815dd0f145ebafded3a438c5) for  X t − 1 {\displaystyle X_{t-1}} ![{\\displaystyle X_{t-1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7cdeab0b9b98bc0b52250537bc0234d7d3de6b60) in the defining equation. Continuing this process _N_ times yields       X t = φ N X t − N + ∑ k = 0 N − 1 φ k ε t − k . {\displaystyle X_{t}=\varphi ^{N}X_{t-N}+\sum _{k=0}^{N-1}\varphi ^{k}\varepsilon _{t-k}.} ![{\\displaystyle X_{t}=\\varphi ^{N}X_{t-N}+\\sum _{k=0}^{N-1}\\varphi ^{k}\\varepsilon _{t-k}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/07c4b3b8a831a9ef5c83ea225c43d179e00d5fce)
For _N_ approaching infinity,  φ N {\displaystyle \varphi ^{N}} ![{\\displaystyle \\varphi ^{N}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a3c7d06db11de79871f23fce1a87a85a61e19f12) will approach zero and:       X t = ∑ k = 0 ∞ φ k ε t − k . {\displaystyle X_{t}=\sum _{k=0}^{\infty }\varphi ^{k}\varepsilon _{t-k}.} ![{\\displaystyle X_{t}=\\sum _{k=0}^{\\infty }\\varphi ^{k}\\varepsilon _{t-k}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5cfa9e0b02bb065b02cf44a0f01480ac9219e358)
It is seen that  X t {\displaystyle X_{t}} ![{\\displaystyle X_{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82120d04dfb3cbadc4912951dd12b5568c9cd8f3) is white noise convolved with the  φ k {\displaystyle \varphi ^{k}} ![{\\displaystyle \\varphi ^{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/718a443a1669e482cf76903e77f49dc3f9a286d7) kernel plus the constant mean. If the white noise  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) is a [Gaussian process](https://en.wikipedia.org/wiki/Gaussian_process "Gaussian process") then  X t {\displaystyle X_{t}} ![{\\displaystyle X_{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82120d04dfb3cbadc4912951dd12b5568c9cd8f3) is also a Gaussian process. In other cases, the [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem "Central limit theorem") indicates that  X t {\displaystyle X_{t}} ![{\\displaystyle X_{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82120d04dfb3cbadc4912951dd12b5568c9cd8f3) will be approximately normally distributed when  φ {\displaystyle \varphi } ![{\\displaystyle \\varphi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/33ee699558d09cf9d653f6351f9fda0b2f4aaa3e) is close to one. 
For  ε t = 0 {\displaystyle \varepsilon _{t}=0} ![{\\displaystyle \\varepsilon _{t}=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/274d9a088f12eef9b2bc0b4c6c797a637dd69e23), the process  X t = φ X t − 1 {\displaystyle X_{t}=\varphi X_{t-1}} ![{\\displaystyle X_{t}=\\varphi X_{t-1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3c5eeeffc952b16bda581094fe1eb451bdc14f4e) will be a [geometric progression](https://en.wikipedia.org/wiki/Geometric_progression "Geometric progression") (_exponential_ growth or decay). In this case, the solution can be found analytically:  X t = a φ t {\displaystyle X_{t}=a\varphi ^{t}} ![{\\displaystyle X_{t}=a\\varphi ^{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/055903c03e931cb2c247112743409af7745932af) whereby  a {\displaystyle a} ![{\\displaystyle a}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ffd2487510aa438433a2579450ab2b3d557e5edc) is an unknown constant ([initial condition](https://en.wikipedia.org/wiki/Initial_condition "Initial condition")). 
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=6 "Edit section: Explicit mean/difference form of AR\(1\) process")]
The AR(1) model is the discrete-time analogy of the continuous [Ornstein-Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein-Uhlenbeck_process "Ornstein-Uhlenbeck process"). It is therefore sometimes useful to understand the properties of the AR(1) model cast in an equivalent form. In this form, the AR(1) model, with process parameter  θ ∈ R {\displaystyle \theta \in \mathbb {R} } ![{\\displaystyle \\theta \\in \\mathbb {R} }](https://wikimedia.org/api/rest_v1/media/math/render/svg/b31351fd5a472b6b13c8ab8228000ff1576fdbdb), is given by       X t + 1 = X t + ( 1 − θ ) ( μ − X t ) + ε t + 1 {\displaystyle X_{t+1}=X_{t}+(1-\theta )(\mu -X_{t})+\varepsilon _{t+1}} ![{\\displaystyle X_{t+1}=X_{t}+\(1-\\theta \)\(\\mu -X_{t}\)+\\varepsilon _{t+1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/306d60853556b6a43b768eebb8308010acf85cff), where  | θ | < 1 {\displaystyle |\theta |<1\,} ![{\\displaystyle |\\theta |<1\\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5780668779972c655ed2ab5186f7e3074ea4530d),  μ := E ( X ) {\displaystyle \mu :=E(X)} ![{\\displaystyle \\mu :=E\(X\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a042b43dac885166129d0b40bc0277c810e742e) is the model mean, and  { ε t } {\displaystyle \\{\varepsilon _{t}\\}} ![{\\displaystyle \\{\\varepsilon _{t}\\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9e567d8e6580293c4caf89372e0a3ba1f3db2d57) is a white-noise process with zero mean and constant variance  σ {\displaystyle \sigma } ![{\\displaystyle \\sigma }](https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36).
By rewriting this as  X t + 1 = θ X t + ( 1 − θ ) μ + ε t + 1 {\displaystyle X_{t+1}=\theta X_{t}+(1-\theta )\mu +\varepsilon _{t+1}} ![{\\displaystyle X_{t+1}=\\theta X_{t}+\(1-\\theta \)\\mu +\\varepsilon _{t+1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f54418bcf2b8928d86d155c73ad9b4e1615a2c6) and then deriving (by induction)  X t + n = θ n X t + ( 1 − θ n ) μ + ∑ i = 1 n ( θ n − i ε t + i ) {\displaystyle X_{t+n}=\theta ^{n}X_{t}+(1-\theta ^{n})\mu +\sum _{i=1}^{n}\left(\theta ^{n-i}\varepsilon _{t+i}\right)} ![{\\displaystyle X_{t+n}=\\theta ^{n}X_{t}+\(1-\\theta ^{n}\)\\mu +\\sum _{i=1}^{n}\\left\(\\theta ^{n-i}\\varepsilon _{t+i}\\right\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6c9bd4f212b2e1cc9c140d40ce29ce017f203820), one can show that       E ⁡ ( X t + n ∣ X t ) = μ [ 1 − θ n ] + X t θ n {\displaystyle \operatorname {E} (X_{t+n}\mid X_{t})=\mu \left[1-\theta ^{n}\right]+X_{t}\theta ^{n}} ![{\\displaystyle \\operatorname {E} \(X_{t+n}\\mid X_{t}\)=\\mu \\left\[1-\\theta ^{n}\\right\]+X_{t}\\theta ^{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/636bc573c78b9440e2f95d8dc9f2bd353f0c17eb) and      Var ⁡ ( X t + n ∣ X t ) = σ 2 1 − θ 2 n 1 − θ 2 . {\displaystyle \operatorname {Var} (X_{t+n}\mid X_{t})=\sigma ^{2}{\frac {1-\theta ^{2n}}{1-\theta ^{2}}}.} ![{\\displaystyle \\operatorname {Var} \(X_{t+n}\\mid X_{t}\)=\\sigma ^{2}{\\frac {1-\\theta ^{2n}}{1-\\theta ^{2}}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5e4b07994da40a114f9617cfea0c59b170c279d8)
## Choosing the maximum lag
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=7 "Edit section: Choosing the maximum lag")]
Main article: [Partial autocorrelation function](https://en.wikipedia.org/wiki/Partial_autocorrelation_function "Partial autocorrelation function")
The partial autocorrelation of an AR(p) process equals zero at lags larger than _p_ , so the appropriate maximum lag _p_ is the one after which the partial autocorrelations are all zero. 
## Calculation of the AR parameters
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=8 "Edit section: Calculation of the AR parameters")]
There are many ways to estimate the coefficients, such as the [ordinary least squares](https://en.wikipedia.org/wiki/Ordinary_least_squares "Ordinary least squares") procedure or [method of moments](https://en.wikipedia.org/wiki/Method_of_moments_\(statistics\) "Method of moments \(statistics\)") (through Yule–Walker equations). 
The AR(_p_) model is given by the equation       X t = ∑ i = 1 p φ i X t − i + ε t . {\displaystyle X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t-i}+\varepsilon _{t}.\,} ![{\\displaystyle X_{t}=\\sum _{i=1}^{p}\\varphi _{i}X_{t-i}+\\varepsilon _{t}.\\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b1a017e273d484ea82c3c0effe3153b1e991a0ef)
It is based on parameters  φ i {\displaystyle \varphi _{i}} ![{\\displaystyle \\varphi _{i}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/70503774fb21be77396899900d3aa1e47d8f9e10) where _i_ = 1, ..., _p_. There is a direct correspondence between these parameters and the covariance function of the process, and this correspondence can be inverted to determine the parameters from the autocorrelation function (which is itself obtained from the covariances). This is done using the Yule–Walker equations. 
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=9 "Edit section: Yule–Walker equations")]
The Yule–Walker equations, named for [Udny Yule](https://en.wikipedia.org/wiki/Udny_Yule "Udny Yule") and [Gilbert Walker](https://en.wikipedia.org/wiki/Gilbert_Walker_\(physicist\) "Gilbert Walker \(physicist\)"),[[14]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-14)[[15]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-15) are the following set of equations.[[16]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-16)      γ m = ∑ k = 1 p φ k γ m − k + σ ε 2 δ m , 0 , {\displaystyle \gamma _{m}=\sum _{k=1}^{p}\varphi _{k}\gamma _{m-k}+\sigma _{\varepsilon }^{2}\delta _{m,0},} ![{\\displaystyle \\gamma _{m}=\\sum _{k=1}^{p}\\varphi _{k}\\gamma _{m-k}+\\sigma _{\\varepsilon }^{2}\\delta _{m,0},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9da60172903d9e7119978e11c9b113da40544a75)
where _m_ = 0, …,  _p_ , yielding _p_ + 1 equations. Here  γ m {\displaystyle \gamma _{m}} ![{\\displaystyle \\gamma _{m}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/27a890b6f03d91a6f3f1033e4ffdf6b2c46c7737) is the autocovariance function of Xt,  σ ε {\displaystyle \sigma _{\varepsilon }} ![{\\displaystyle \\sigma _{\\varepsilon }}](https://wikimedia.org/api/rest_v1/media/math/render/svg/04852f481494a445c9f5b9082df1ead002c098a2) is the standard deviation of the input noise process, and  δ m , 0 {\displaystyle \delta _{m,0}} ![{\\displaystyle \\delta _{m,0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e1370316eefa8164f8231f804f30d9e9a15cc652) is the [Kronecker delta function](https://en.wikipedia.org/wiki/Kronecker_delta_function "Kronecker delta function"). 
Because the last part of an individual equation is non-zero only if _m_ = 0, the set of equations can be solved by representing the equations for _m_ > 0 in matrix form, thus getting the equation       [ γ 1 γ 2 γ 3 ⋮ γ p ] = [ γ 0 γ − 1 γ − 2 ⋯ γ 1 γ 0 γ − 1 ⋯ γ 2 γ 1 γ 0 ⋯ ⋮ ⋮ ⋮ ⋱ γ p − 1 γ p − 2 γ p − 3 ⋯ ] [ φ 1 φ 2 φ 3 ⋮ φ p ] {\displaystyle {\begin{bmatrix}\gamma _{1}\\\\\gamma _{2}\\\\\gamma _{3}\\\\\vdots \\\\\gamma _{p}\\\\\end{bmatrix}}={\begin{bmatrix}\gamma _{0}&\gamma _{-1}&\gamma _{-2}&\cdots \\\\\gamma _{1}&\gamma _{0}&\gamma _{-1}&\cdots \\\\\gamma _{2}&\gamma _{1}&\gamma _{0}&\cdots \\\\\vdots &\vdots &\vdots &\ddots \\\\\gamma _{p-1}&\gamma _{p-2}&\gamma _{p-3}&\cdots \\\\\end{bmatrix}}{\begin{bmatrix}\varphi _{1}\\\\\varphi _{2}\\\\\varphi _{3}\\\\\vdots \\\\\varphi _{p}\\\\\end{bmatrix}}} ![{\\displaystyle {\\begin{bmatrix}\\gamma _{1}\\\\\\gamma _{2}\\\\\\gamma _{3}\\\\\\vdots \\\\\\gamma _{p}\\\\\\end{bmatrix}}={\\begin{bmatrix}\\gamma _{0}&\\gamma _{-1}&\\gamma _{-2}&\\cdots \\\\\\gamma _{1}&\\gamma _{0}&\\gamma _{-1}&\\cdots \\\\\\gamma _{2}&\\gamma _{1}&\\gamma _{0}&\\cdots \\\\\\vdots &\\vdots &\\vdots &\\ddots \\\\\\gamma _{p-1}&\\gamma _{p-2}&\\gamma _{p-3}&\\cdots \\\\\\end{bmatrix}}{\\begin{bmatrix}\\varphi _{1}\\\\\\varphi _{2}\\\\\\varphi _{3}\\\\\\vdots \\\\\\varphi _{p}\\\\\\end{bmatrix}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3a564a8ed89ab0e811cec86e6381723792950663)
which can be solved for all  { φ m ; m = 1 , 2 , … , p } . {\displaystyle \\{\varphi _{m};m=1,2,\dots ,p\\}.} ![{\\displaystyle \\{\\varphi _{m};m=1,2,\\dots ,p\\}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a852eb40a2580da26a00424bfa85c14c077bc73e) The remaining equation for _m_ = 0 is       γ 0 = ∑ k = 1 p φ k γ − k + σ ε 2 , {\displaystyle \gamma _{0}=\sum _{k=1}^{p}\varphi _{k}\gamma _{-k}+\sigma _{\varepsilon }^{2},} ![{\\displaystyle \\gamma _{0}=\\sum _{k=1}^{p}\\varphi _{k}\\gamma _{-k}+\\sigma _{\\varepsilon }^{2},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9b026ab9a1802d7f6365a76f22b966a46f39f3f4)
which, once  { φ m ; m = 1 , 2 , … , p } {\displaystyle \\{\varphi _{m};m=1,2,\dots ,p\\}} ![{\\displaystyle \\{\\varphi _{m};m=1,2,\\dots ,p\\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/11b162c79b064fc3de8d868c0a5210897b051f0f) are known, can be solved for  σ ε 2 . {\displaystyle \sigma _{\varepsilon }^{2}.} ![{\\displaystyle \\sigma _{\\varepsilon }^{2}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/aa5d61c2a70c33444023a77f42f7502a2abd7c18)
An alternative formulation is in terms of the [autocorrelation function](https://en.wikipedia.org/wiki/Autocorrelation_function "Autocorrelation function"). The AR parameters are determined by the first _p_ +1 elements  ρ ( τ ) {\displaystyle \rho (\tau )} ![{\\displaystyle \\rho \(\\tau \)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7f1b4786ec22c80e8b5d81429869524e2fadca5e) of the autocorrelation function. The full autocorrelation function can then be derived by recursively calculating [[17]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-Storch-17)      ρ ( τ ) = ∑ k = 1 p φ k ρ ( k − τ ) {\displaystyle \rho (\tau )=\sum _{k=1}^{p}\varphi _{k}\rho (k-\tau )} ![{\\displaystyle \\rho \(\\tau \)=\\sum _{k=1}^{p}\\varphi _{k}\\rho \(k-\\tau \)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b7510506c4854869e268ae4a004ffdeaf07a0713)
Examples for some Low-order AR(_p_) processes 
  * _p_ =1 
    * γ 1 = φ 1 γ 0 {\displaystyle \gamma _{1}=\varphi _{1}\gamma _{0}} ![{\\displaystyle \\gamma _{1}=\\varphi _{1}\\gamma _{0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7e8bf2eecd26d68040d14b4395e6e6ee608d80b5)
    * Hence  ρ 1 = γ 1 / γ 0 = φ 1 {\displaystyle \rho _{1}=\gamma _{1}/\gamma _{0}=\varphi _{1}} ![{\\displaystyle \\rho _{1}=\\gamma _{1}/\\gamma _{0}=\\varphi _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b497cf1e359dd28af10fadeb373548eb34656b47)
  * _p_ =2 
    * The Yule–Walker equations for an AR(2) process are       γ 1 = φ 1 γ 0 + φ 2 γ − 1 {\displaystyle \gamma _{1}=\varphi _{1}\gamma _{0}+\varphi _{2}\gamma _{-1}} ![{\\displaystyle \\gamma _{1}=\\varphi _{1}\\gamma _{0}+\\varphi _{2}\\gamma _{-1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d8a22c7a06835e594cec72e5c83a633b812064b5)      γ 2 = φ 1 γ 1 + φ 2 γ 0 {\displaystyle \gamma _{2}=\varphi _{1}\gamma _{1}+\varphi _{2}\gamma _{0}} ![{\\displaystyle \\gamma _{2}=\\varphi _{1}\\gamma _{1}+\\varphi _{2}\\gamma _{0}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cf33ac37c5209d496139c69ee8a0fb2fd9fa4bdf)
      * Remember that  γ − k = γ k {\displaystyle \gamma _{-k}=\gamma _{k}} ![{\\displaystyle \\gamma _{-k}=\\gamma _{k}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8ce33584a8a0c4817bba5a476b369ab6d1ba76fb)
      * Using the first equation yields  ρ 1 = γ 1 / γ 0 = φ 1 1 − φ 2 {\displaystyle \rho _{1}=\gamma _{1}/\gamma _{0}={\frac {\varphi _{1}}{1-\varphi _{2}}}} ![{\\displaystyle \\rho _{1}=\\gamma _{1}/\\gamma _{0}={\\frac {\\varphi _{1}}{1-\\varphi _{2}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/37eeb70989f5c088e165c97a2be5dbbaacb2c291)
      * Using the recursion formula yields  ρ 2 = γ 2 / γ 0 = φ 1 2 − φ 2 2 + φ 2 1 − φ 2 {\displaystyle \rho _{2}=\gamma _{2}/\gamma _{0}={\frac {\varphi _{1}^{2}-\varphi _{2}^{2}+\varphi _{2}}{1-\varphi _{2}}}} ![{\\displaystyle \\rho _{2}=\\gamma _{2}/\\gamma _{0}={\\frac {\\varphi _{1}^{2}-\\varphi _{2}^{2}+\\varphi _{2}}{1-\\varphi _{2}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e7156ced938798e237ac752692eb1e07195dbc2)


### Estimation of AR parameters
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=10 "Edit section: Estimation of AR parameters")]
The above equations (the Yule–Walker equations) provide several routes to estimating the parameters of an AR(_p_) model, by replacing the theoretical covariances with estimated values.[[18]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-18) Some of these variants can be described as follows: 
  * Estimation of autocovariances or autocorrelations. Here each of these terms is estimated separately, using conventional estimates. There are different ways of doing this and the choice between these affects the properties of the estimation scheme. For example, negative estimates of the variance can be produced by some choices.
  * Formulation as a [least squares regression](https://en.wikipedia.org/wiki/Least_squares_regression "Least squares regression") problem in which an ordinary least squares prediction problem is constructed, basing prediction of values of _X_ _t_ on the _p_ previous values of the same series. This can be thought of as a forward-prediction scheme. The [normal equations](https://en.wikipedia.org/wiki/Normal_equations "Normal equations") for this problem can be seen to correspond to an approximation of the matrix form of the Yule–Walker equations in which each appearance of an autocovariance of the same lag is replaced by a slightly different estimate.
  * Formulation as an extended form of ordinary least squares prediction problem. Here two sets of prediction equations are combined into a single estimation scheme and a single set of normal equations. One set is the set of forward-prediction equations and the other is a corresponding set of backward prediction equations, relating to the backward representation of the AR model:

         X t = ∑ i = 1 p φ i X t + i + ε t ∗ . {\displaystyle X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t+i}+\varepsilon _{t}^{*}\,.} ![{\\displaystyle X_{t}=\\sum _{i=1}^{p}\\varphi _{i}X_{t+i}+\\varepsilon _{t}^{*}\\,.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c77daca7a31182f4b78f428aafd3bcebb460b400)     Here predicted values of _X_ _t_ would be based on the _p_ future values of the same series.[_[clarification needed](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")_] This way of estimating the AR parameters is due to John Parker Burg,[[19]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-Burg-19) and is called the Burg method:[[20]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-Brockwell-20) Burg and later authors called these particular estimates "maximum entropy estimates",[[21]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-Burg1-21) but the reasoning behind this applies to the use of any set of estimated AR parameters. Compared to the estimation scheme using only the forward prediction equations, different estimates of the autocovariances are produced, and the estimates have different stability properties. Burg estimates are particularly associated with [maximum entropy spectral estimation](https://en.wikipedia.org/wiki/Maximum_entropy_spectral_estimation "Maximum entropy spectral estimation").[[22]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-Bos-22)
Other possible approaches to estimation include [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation "Maximum likelihood estimation"). Two distinct variants of maximum likelihood are available: in one (broadly equivalent to the forward prediction least squares scheme) the likelihood function considered is that corresponding to the conditional distribution of later values in the series given the initial _p_ values in the series; in the second, the likelihood function considered is that corresponding to the unconditional joint distribution of all the values in the observed series. Substantial differences in the results of these approaches can occur if the observed series is short, or if the process is close to non-stationarity. 
## Spectrum
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=11 "Edit section: Spectrum")]
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/AutocorrTimeAr.svg/250px-AutocorrTimeAr.svg.png)](https://en.wikipedia.org/wiki/File:AutocorrTimeAr.svg) [![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/AutoCorrAR.svg/250px-AutoCorrAR.svg.png)](https://en.wikipedia.org/wiki/File:AutoCorrAR.svg)
The [power spectral density](https://en.wikipedia.org/wiki/Spectral_density#Power_spectral_density "Spectral density") (PSD) of an AR(_p_) process with noise variance  V a r ( Z t ) = σ Z 2 {\displaystyle \mathrm {Var} (Z_{t})=\sigma _{Z}^{2}} ![{\\displaystyle \\mathrm {Var} \(Z_{t}\)=\\sigma _{Z}^{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fcf6634824713d3cfd153951776fe39e92578b21) is[[17]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-Storch-17)      S ( f ) = σ Z 2 | 1 − ∑ k = 1 p φ k e − i 2 π f k | 2 . {\displaystyle S(f)={\frac {\sigma _{Z}^{2}}{|1-\sum _{k=1}^{p}\varphi _{k}e^{-i2\pi fk}|^{2}}}.} ![{\\displaystyle S\(f\)={\\frac {\\sigma _{Z}^{2}}{|1-\\sum _{k=1}^{p}\\varphi _{k}e^{-i2\\pi fk}|^{2}}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/42f50b7ac757b2de256f1e9ff1571e969884c257)
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=12 "Edit section: AR\(0\)")]
For white noise (AR(0))       S ( f ) = σ Z 2 . {\displaystyle S(f)=\sigma _{Z}^{2}.} ![{\\displaystyle S\(f\)=\\sigma _{Z}^{2}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/06468b780d3e82778416cc74ff45f2bb6298547f)
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=13 "Edit section: AR\(1\)")]
For AR(1)       S ( f ) = σ Z 2 | 1 − φ 1 e − 2 π i f | 2 = σ Z 2 1 + φ 1 2 − 2 φ 1 cos ⁡ 2 π f {\displaystyle S(f)={\frac {\sigma _{Z}^{2}}{|1-\varphi _{1}e^{-2\pi if}|^{2}}}={\frac {\sigma _{Z}^{2}}{1+\varphi _{1}^{2}-2\varphi _{1}\cos 2\pi f}}} ![{\\displaystyle S\(f\)={\\frac {\\sigma _{Z}^{2}}{|1-\\varphi _{1}e^{-2\\pi if}|^{2}}}={\\frac {\\sigma _{Z}^{2}}{1+\\varphi _{1}^{2}-2\\varphi _{1}\\cos 2\\pi f}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fe899e2c744e152309b413956cb163d64218246b)
  * If  φ 1 > 0 {\displaystyle \varphi _{1}>0} ![{\\displaystyle \\varphi _{1}>0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/abe87447932492440bc26bb36dd9106b3a00b94e) there is a single spectral peak at  f = 0 {\displaystyle f=0} ![{\\displaystyle f=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1ee0fdf0f50fcba5afe3e856fcc7dc6acfa61014), often referred to as [red noise](https://en.wikipedia.org/wiki/Red_noise "Red noise"). As  φ 1 {\displaystyle \varphi _{1}} ![{\\displaystyle \\varphi _{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d7daf493c8f6ef669c04c7b9715532fc35d12d60) becomes nearer 1, there is stronger power at low frequencies, i.e. larger time lags. This is then a low-pass filter, when applied to full spectrum light, everything except for the red light will be filtered.
  * If  φ 1 < 0 {\displaystyle \varphi _{1}<0} ![{\\displaystyle \\varphi _{1}<0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/df3bd2845ccc8efc15e3eb61ca848ac2af258802) there is a minimum at  f = 0 {\displaystyle f=0} ![{\\displaystyle f=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1ee0fdf0f50fcba5afe3e856fcc7dc6acfa61014), often referred to as [blue noise](https://en.wikipedia.org/wiki/Blue_noise "Blue noise"). This similarly acts as a high-pass filter, everything except for blue light will be filtered.


[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=14 "Edit section: AR\(2\)")]
The behavior of an AR(2) process is determined entirely by the roots of it [characteristic equation](https://en.wikipedia.org/wiki/Characteristic_equation_\(calculus\) "Characteristic equation \(calculus\)"), which is expressed in terms of the [lag operator](https://en.wikipedia.org/wiki/Lag_operator "Lag operator") as:       1 − φ 1 B − φ 2 B 2 = 0 , {\displaystyle 1-\varphi _{1}B-\varphi _{2}B^{2}=0,} ![{\\displaystyle 1-\\varphi _{1}B-\\varphi _{2}B^{2}=0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7af3e38e0138f8bcb67856401cdb332e075def5e)
or equivalently by the poles of its [transfer function](https://en.wikipedia.org/wiki/Transfer_function "Transfer function"), which is defined in the [Z domain](https://en.wikipedia.org/wiki/Z-transform "Z-transform") by:       H z = ( 1 − φ 1 z − 1 − φ 2 z − 2 ) − 1 . {\displaystyle H_{z}=(1-\varphi _{1}z^{-1}-\varphi _{2}z^{-2})^{-1}.} ![{\\displaystyle H_{z}=\(1-\\varphi _{1}z^{-1}-\\varphi _{2}z^{-2}\)^{-1}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/42a3d758905d4bf4af1b22f12d47e6499b3e00b2)
It follows that the poles are values of z satisfying:       1 − φ 1 z − 1 − φ 2 z − 2 = 0 , {\displaystyle 1-\varphi _{1}z^{-1}-\varphi _{2}z^{-2}=0,} ![{\\displaystyle 1-\\varphi _{1}z^{-1}-\\varphi _{2}z^{-2}=0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e0a91ffc13c61cd3e4979ac09ec68cc2088ecd3d)
which yields:       z 1 , z 2 = 1 2 φ 2 ( φ 1 ± φ 1 2 + 4 φ 2 ) . {\displaystyle z_{1},z_{2}={\frac {1}{2\varphi _{2}}}\left(\varphi _{1}\pm {\sqrt {\varphi _{1}^{2}+4\varphi _{2}}}\,\right).} ![{\\displaystyle z_{1},z_{2}={\\frac {1}{2\\varphi _{2}}}\\left\(\\varphi _{1}\\pm {\\sqrt {\\varphi _{1}^{2}+4\\varphi _{2}}}\\,\\right\).}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fc48c4058d25c3268d5175f4a10da1f44e4f58b4)
z 1 {\displaystyle z_{1}} ![{\\displaystyle z_{1}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3621e468231ab352b7caa30bcf0ce9b452241a6) and  z 2 {\displaystyle z_{2}} ![{\\displaystyle z_{2}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5abf655fa14f7ea44ad0ca781b59ff59c5f49117) are the reciprocals of the characteristic roots, as well as the eigenvalues of the temporal update matrix:       [ φ 1 φ 2 1 0 ] {\displaystyle {\begin{bmatrix}\varphi _{1}&\varphi _{2}\\\1&0\end{bmatrix}}} ![{\\displaystyle {\\begin{bmatrix}\\varphi _{1}&\\varphi _{2}\\\\1&0\\end{bmatrix}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9f329235be209f01d37f96c2c92341066d0524da)
AR(2) processes can be split into three groups depending on the characteristics of their roots/poles: 
  * When  φ 1 2 + 4 φ 2 < 0 {\displaystyle \varphi _{1}^{2}+4\varphi _{2}<0} ![{\\displaystyle \\varphi _{1}^{2}+4\\varphi _{2}<0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0458ca96d21393755f25e547fb527f92a5b25272), the process has a pair of complex-conjugate poles, creating a mid-frequency peak at:

     f ∗ = 1 2 π cos − 1 ⁡ ( φ 1 2 − φ 2 ) , {\displaystyle f^{*}={\frac {1}{2\pi }}\cos ^{-1}\left({\frac {\varphi _{1}}{2{\sqrt {-\varphi _{2}}}}}\right),} ![{\\displaystyle f^{*}={\\frac {1}{2\\pi }}\\cos ^{-1}\\left\({\\frac {\\varphi _{1}}{2{\\sqrt {-\\varphi _{2}}}}}\\right\),}](https://wikimedia.org/api/rest_v1/media/math/render/svg/57755a084516b69b752f9c6b507e9055769b7b5a)
with bandwidth about the peak inversely proportional to the moduli of the poles:       | z 1 | = | z 2 | = − φ 2 . {\displaystyle |z_{1}|=|z_{2}|={\sqrt {-\varphi _{2}}}.} ![{\\displaystyle |z_{1}|=|z_{2}|={\\sqrt {-\\varphi _{2}}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ad6806931fd224663b11643262068e6814881447)
The terms involving square roots are all real in the case of complex poles since they exist only when  φ 2 < 0 {\displaystyle \varphi _{2}<0} ![{\\displaystyle \\varphi _{2}<0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fc7620690c960582c0f901f83633ccd7e06e3f8c). 
Otherwise the process has real roots, and: 
  * When  φ 1 > 0 {\displaystyle \varphi _{1}>0} ![{\\displaystyle \\varphi _{1}>0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/abe87447932492440bc26bb36dd9106b3a00b94e) it acts as a low-pass filter on the white noise with a spectral peak at  f = 0 {\displaystyle f=0} ![{\\displaystyle f=0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1ee0fdf0f50fcba5afe3e856fcc7dc6acfa61014)
  * When  φ 1 < 0 {\displaystyle \varphi _{1}<0} ![{\\displaystyle \\varphi _{1}<0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/df3bd2845ccc8efc15e3eb61ca848ac2af258802) it acts as a high-pass filter on the white noise with a spectral peak at  f = 1 / 2 {\displaystyle f=1/2} ![{\\displaystyle f=1/2}](https://wikimedia.org/api/rest_v1/media/math/render/svg/09c9d48b46b004abc15e441ada41e3ac9b8d3e40).


The process is non-stationary when the poles are on or outside the unit circle, or equivalently when the characteristic roots are on or inside the unit circle. The process is stable when the poles are strictly within the unit circle (roots strictly outside the unit circle), or equivalently when the coefficients are in the triangle  − 1 ≤ φ 2 ≤ 1 − | φ 1 | {\displaystyle -1\leq \varphi _{2}\leq 1-|\varphi _{1}|} ![{\\displaystyle -1\\leq \\varphi _{2}\\leq 1-|\\varphi _{1}|}](https://wikimedia.org/api/rest_v1/media/math/render/svg/174a4fea8bdb965bfce378f7c22e1333141e85ea). 
The full PSD function can be expressed in real form as:       S ( f ) = σ Z 2 1 + φ 1 2 + φ 2 2 − 2 φ 1 ( 1 − φ 2 ) cos ⁡ ( 2 π f ) − 2 φ 2 cos ⁡ ( 4 π f ) {\displaystyle S(f)={\frac {\sigma _{Z}^{2}}{1+\varphi _{1}^{2}+\varphi _{2}^{2}-2\varphi _{1}(1-\varphi _{2})\cos(2\pi f)-2\varphi _{2}\cos(4\pi f)}}} ![{\\displaystyle S\(f\)={\\frac {\\sigma _{Z}^{2}}{1+\\varphi _{1}^{2}+\\varphi _{2}^{2}-2\\varphi _{1}\(1-\\varphi _{2}\)\\cos\(2\\pi f\)-2\\varphi _{2}\\cos\(4\\pi f\)}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a013a00f38c6fa6be16d25f4b30ed3842b88a04e)
## Implementations in statistics packages
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=15 "Edit section: Implementations in statistics packages")]
  * [R](https://en.wikipedia.org/wiki/R_\(programming_language\) "R \(programming language\)") – the _stats_ package includes _ar_ function;[[23]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-23) the _astsa_ package includes _sarima_ function to fit various models including AR.[[24]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-:0-24)
  * [MATLAB](https://en.wikipedia.org/wiki/MATLAB "MATLAB") – the Econometrics Toolbox[[25]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-25) and System Identification Toolbox[[26]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-26) include AR models.[[27]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-27)
  * [MATLAB](https://en.wikipedia.org/wiki/MATLAB "MATLAB") and [Octave](https://en.wikipedia.org/wiki/GNU_Octave "GNU Octave") – the _TSA_ toolbox contains several estimation functions for uni-variate, [multivariate](https://en.wikipedia.org/wiki/Multivariate_statistics "Multivariate statistics"), and adaptive AR models.[[28]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-28)
  * [PyMC](https://en.wikipedia.org/wiki/PyMC "PyMC")3 – the Bayesian statistics and probabilistic programming framework supports AR modes with _p_ lags.
  * _bayesloop_ – supports parameter inference and model selection for the AR-1 process with time-varying parameters.[[29]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-29)
  * [Python](https://en.wikipedia.org/wiki/Python_\(programming_language\) "Python \(programming language\)") – statsmodels.org hosts an AR model.[[30]](https://en.wikipedia.org/wiki/Autoregressive_model#cite_note-30)


## Impulse response
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=16 "Edit section: Impulse response")]
The [impulse response](https://en.wikipedia.org/wiki/Impulse_response "Impulse response") of a system is the change in an evolving variable in response to a change in the value of a shock term _k_ periods earlier, as a function of _k_. Since the AR model is a special case of the vector autoregressive model, the computation of the impulse response in [vector autoregression#impulse response](https://en.wikipedia.org/wiki/Vector_autoregression#Impulse_response "Vector autoregression") applies here. 
##  _n_ -step-ahead forecasting
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=17 "Edit section: n-step-ahead forecasting")]
Once the parameters of the autoregression       X t = ∑ i = 1 p φ i X t − i + ε t {\displaystyle X_{t}=\sum _{i=1}^{p}\varphi _{i}X_{t-i}+\varepsilon _{t}\,} ![{\\displaystyle X_{t}=\\sum _{i=1}^{p}\\varphi _{i}X_{t-i}+\\varepsilon _{t}\\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/989ee564796d9883fe00ba3d1faf373a731c0065)
have been estimated, the autoregression can be used to forecast an arbitrary number of periods into the future. First use _t_ to refer to the first period for which data is not yet available; substitute the known preceding values _X_ _t-i_ for _i=_ 1, ..., _p_ into the autoregressive equation while setting the error term  ε t {\displaystyle \varepsilon _{t}} ![{\\displaystyle \\varepsilon _{t}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7c1ff8b8945e6a4fccf6071f806b9ef232492b9a) equal to zero (because we forecast _X_ _t_ to equal its expected value, and the expected value of the unobserved error term is zero). The output of the autoregressive equation is the forecast for the first unobserved period. Next, use _t_ to refer to the _next_ period for which data is not yet available; again the autoregressive equation is used to make the forecast, with one difference: the value of _X_ one period prior to the one now being forecast is not known, so its expected value—the predicted value arising from the previous forecasting step—is used instead. Then for future periods the same procedure is used, each time using one more forecast value on the right side of the predictive equation until, after _p_ predictions, all _p_ right-side values are predicted values from preceding steps. 
There are four sources of uncertainty regarding predictions obtained in this manner: (1) uncertainty as to whether the autoregressive model is the correct model; (2) uncertainty about the accuracy of the forecasted values that are used as lagged values in the right side of the autoregressive equation; (3) uncertainty about the true values of the autoregressive coefficients; and (4) uncertainty about the value of the error term  ε t {\displaystyle \varepsilon _{t}\,} ![{\\displaystyle \\varepsilon _{t}\\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0dddd630dd121297ad959b33a2adf8d58c3101ea) for the period being predicted. Each of the last three can be quantified and combined to give a [confidence interval](https://en.wikipedia.org/wiki/Confidence_interval "Confidence interval") for the _n_ -step-ahead predictions; the confidence interval will become wider as _n_ increases because of the use of an increasing number of estimated values for the right-side variables. 
## See also
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=18 "Edit section: See also")]
  * [Moving average model](https://en.wikipedia.org/wiki/Moving_average_model "Moving average model")
  * [Linear difference equation](https://en.wikipedia.org/wiki/Linear_difference_equation "Linear difference equation")
  * [Predictive analytics](https://en.wikipedia.org/wiki/Predictive_analytics "Predictive analytics")
  * [Linear predictive coding](https://en.wikipedia.org/wiki/Linear_predictive_coding "Linear predictive coding")
  * [Resonance](https://en.wikipedia.org/wiki/Resonance "Resonance")
  * [Levinson recursion](https://en.wikipedia.org/wiki/Levinson_recursion "Levinson recursion")
  * [Ornstein–Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process "Ornstein–Uhlenbeck process")
  * [Infinite impulse response](https://en.wikipedia.org/wiki/Infinite_impulse_response "Infinite impulse response")
  * [PagedAttention](https://en.wikipedia.org/wiki/PagedAttention "PagedAttention") / [vAttention](https://en.wikipedia.org/wiki/PagedAttention#vAttention "PagedAttention") — attention algorithms for efficient serving of large language models


## Notes
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=19 "Edit section: Notes")]
  1. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-1)** Souza, Douglas Baptista de; Leao, Bruno Paes (26 October 2023). ["Data Augmentation of Sensor Time Series using Time-varying Autoregressive Processes"](https://doi.org/10.36001%2Fphmconf.2023.v15i1.3565). _Annual Conference of the PHM Society_. **15** (1). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.36001/phmconf.2023.v15i1.3565](https://doi.org/10.36001%2Fphmconf.2023.v15i1.3565).
  2. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-2)** Souza, Douglas Baptista de; Leao, Bruno Paes (5 November 2024). "Data Augmentation of Multivariate Sensor Time Series using Autoregressive Models and Application to Failure Prognostics". _Annual Conference of the PHM Society_. **16** (1). [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2410.16419](https://arxiv.org/abs/2410.16419). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.36001/phmconf.2024.v16i1.4145](https://doi.org/10.36001%2Fphmconf.2024.v16i1.4145).
  3. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-3)** Diodato, Nazzareno; Di Salvo, Cristina; Bellocchi, Gianni (18 March 2025). ["Climate driven generative time-varying model for improved decadal storm power predictions in the Mediterranean"](https://doi.org/10.1038%2Fs43247-025-02196-2). _Communications Earth & Environment_. **6** (1): 212. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2025ComEE...6..212D](https://ui.adsabs.harvard.edu/abs/2025ComEE...6..212D). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1038/s43247-025-02196-2](https://doi.org/10.1038%2Fs43247-025-02196-2).
  4. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-4)** Inayati, Syarifah; Iriawan, Nur (31 December 2024). ["Time-Varying Autoregressive Models for Economic Forecasting"](https://doi.org/10.11113%2Fmatematika.v40.n3.1654). _Matematika_ : 131–142. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.11113/matematika.v40.n3.1654](https://doi.org/10.11113%2Fmatematika.v40.n3.1654).
  5. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-5)** Jia, Zhixuan; Li, Wang; Jiang, Yunlong; Liu, Xingshen (9 July 2025). ["The Use of Minimization Solvers for Optimizing Time-Varying Autoregressive Models and Their Applications in Finance"](https://doi.org/10.3390%2Fmath13142230). _Mathematics_. **13** (14): 2230. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.3390/math13142230](https://doi.org/10.3390%2Fmath13142230).
  6. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-6)** Baptista de Souza, Douglas; Kuhn, Eduardo Vinicius; Seara, Rui (January 2019). "A Time-Varying Autoregressive Model for Characterizing Nonstationary Processes". _IEEE Signal Processing Letters_. **26** (1): 134–138. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2019ISPL...26..134B](https://ui.adsabs.harvard.edu/abs/2019ISPL...26..134B). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1109/LSP.2018.2880086](https://doi.org/10.1109%2FLSP.2018.2880086).
  7. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-7)** Wang, Shihan; Chen, Tao; Wang, Hongjian (17 March 2023). ["IDBD-Based Beamforming Algorithm for Improving the Performance of Phased Array Radar in Nonstationary Environments"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10052024). _Sensors_. **23** (6): 3211. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2023Senso..23.3211W](https://ui.adsabs.harvard.edu/abs/2023Senso..23.3211W). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.3390/s23063211](https://doi.org/10.3390%2Fs23063211). [PMC](https://en.wikipedia.org/wiki/PMC_\(identifier\) "PMC \(identifier\)") [10052024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10052024). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID \(identifier\)") [36991922](https://pubmed.ncbi.nlm.nih.gov/36991922).
  8. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-8)** Abramovich, Yuri I.; Spencer, Nicholas K.; Turley, Michael D. E. (April 2007). "Time-Varying Autoregressive (TVAR) Models for Multiple Radar Observations". _IEEE Transactions on Signal Processing_. **55** (4): 1298–1311. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2007ITSP...55.1298A](https://ui.adsabs.harvard.edu/abs/2007ITSP...55.1298A). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1109/TSP.2006.888064](https://doi.org/10.1109%2FTSP.2006.888064).
  9. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-9)** Gutierrez, D.; Salazar-Varas, R. (August 2011). "EEG signal classification using time-varying autoregressive models and common spatial patterns". _2011 Annual International Conference of the IEEE Engineering in Medicine and Biology Society_. pp. 6585–6588. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1109/IEMBS.2011.6091624](https://doi.org/10.1109%2FIEMBS.2011.6091624). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-4577-1589-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4577-1589-1 "Special:BookSources/978-1-4577-1589-1"). [PMID](https://en.wikipedia.org/wiki/PMID_\(identifier\) "PMID \(identifier\)") [22255848](https://pubmed.ncbi.nlm.nih.gov/22255848).
  10. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-10)** Box, George E. P. (1994). _Time series analysis : forecasting and control_. Gwilym M. Jenkins, Gregory C. Reinsel (3rd ed.). Englewood Cliffs, N.J.: Prentice Hall. p. 54. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-13-060774-6](https://en.wikipedia.org/wiki/Special:BookSources/0-13-060774-6 "Special:BookSources/0-13-060774-6"). [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC \(identifier\)") [28888762](https://search.worldcat.org/oclc/28888762).
  11. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-11)** [Shumway, Robert H.](https://en.wikipedia.org/wiki/Robert_H._Shumway "Robert H. Shumway") (2000). _Time series analysis and its applications_. David S. Stoffer. New York: Springer. pp. 90–91. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-387-98950-1](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98950-1 "Special:BookSources/0-387-98950-1"). [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC \(identifier\)") [42392178](https://search.worldcat.org/oclc/42392178).
  12. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-12)** Shumway, Robert H.; Stoffer, David (2010). _Time series analysis and its applications : with R examples_ (3rd ed.). Springer. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1441978646](https://en.wikipedia.org/wiki/Special:BookSources/978-1441978646 "Special:BookSources/978-1441978646").
  13. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-13)** Lai, Dihui; and Lu, Bingfeng; ["Understanding Autoregressive Model for Time Series as a Deterministic Dynamic System"](https://www.soa.org/globalassets/assets/library/newsletters/predictive-analytics-and-futurism/2017/june/2017-predictive-analytics-iss15-lai-lu.pdf) [Archived](https://web.archive.org/web/20230324041726/https://www.soa.org/globalassets/assets/library/newsletters/predictive-analytics-and-futurism/2017/june/2017-predictive-analytics-iss15-lai-lu.pdf) 2023-03-24 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine"), in _Predictive Analytics and Futurism_ , June 2017, number 15, June 2017, pages 7-9
  14. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-14)** Yule, G. Udny (1927) ["On a Method of Investigating Periodicities in Disturbed Series, with Special Reference to Wolfer's Sunspot Numbers"](http://visualiseur.bnf.fr/Visualiseur?Destination=Gallica&O=NUMM-56031) [Archived](https://web.archive.org/web/20110514094546/http://visualiseur.bnf.fr/Visualiseur?Destination=Gallica&O=NUMM-56031) 2011-05-14 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine"), _[Philosophical Transactions of the Royal Society](https://en.wikipedia.org/wiki/Philosophical_Transactions_of_the_Royal_Society "Philosophical Transactions of the Royal Society") of London_, Ser. A, Vol. 226, 267–298.]
  15. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-15)** Walker, Gilbert (1931) ["On Periodicity in Series of Related Terms"](http://visualiseur.bnf.fr/Visualiseur?Destination=Gallica&O=NUMM-56224) [Archived](https://web.archive.org/web/20110607170511/http://visualiseur.bnf.fr/Visualiseur?Destination=Gallica&O=NUMM-56224) 2011-06-07 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine"), _[Proceedings of the Royal Society](https://en.wikipedia.org/wiki/Proceedings_of_the_Royal_Society "Proceedings of the Royal Society") of London_, Ser. A, Vol. 131, 518–532.
  16. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-16)** Theodoridis, Sergios (2015-04-10). "Chapter 1. Probability and Stochastic Processes". _Machine Learning: A Bayesian and Optimization Perspective_. Academic Press, 2015. pp. 9–51. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-12-801522-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-12-801522-3 "Special:BookSources/978-0-12-801522-3").
  17. ^ [_**a**_](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-Storch_17-0) [_**b**_](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-Storch_17-1) Von Storch, Hans; Zwiers, Francis W. (2001). _Statistical analysis in climate research_. Cambridge University Press. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1017/CBO9780511612336](https://doi.org/10.1017%2FCBO9780511612336). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-521-01230-9](https://en.wikipedia.org/wiki/Special:BookSources/0-521-01230-9 "Special:BookSources/0-521-01230-9").[_[page needed](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources")_]
  18. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-18)** Eshel, Gidon. ["The Yule Walker Equations for the AR Coefficients"](http://www-stat.wharton.upenn.edu/~steele/Courses/956/Resource/YWSourceFiles/YW-Eshel.pdf) (PDF). _stat.wharton.upenn.edu_. [Archived](https://web.archive.org/web/20180713135223/http://www-stat.wharton.upenn.edu/~steele/Courses/956/Resource/YWSourceFiles/YW-Eshel.pdf) (PDF) from the original on 2018-07-13. Retrieved 2019-01-27.
  19. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-Burg_19-0)** Burg, John Parker (1968); "A new analysis technique for time series data", in _Modern Spectrum Analysis_ (Edited by D. G. Childers), NATO Advanced Study Institute of Signal Processing with emphasis on Underwater Acoustics. IEEE Press, New York.
  20. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-Brockwell_20-0)** Brockwell, Peter J.; Dahlhaus, Rainer; Trindade, A. Alexandre (2005). ["Modified Burg Algorithms for Multivariate Subset Autoregression"](https://web.archive.org/web/20121021015413/http://www3.stat.sinica.edu.tw/statistica/oldpdf/A15n112.pdf) (PDF). _Statistica Sinica_. **15** : 197–213. Archived from [the original](http://www3.stat.sinica.edu.tw/statistica/oldpdf/A15n112.pdf) (PDF) on 2012-10-21.
  21. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-Burg1_21-0)** Burg, John Parker (1967) "Maximum Entropy Spectral Analysis", _Proceedings of the 37th Meeting of the Society of Exploration Geophysicists_ , Oklahoma City, Oklahoma.
  22. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-Bos_22-0)** Bos, Robert; De Waele, Stijn; Broersen, Piet M. T. (2002). ["Autoregressive spectral estimation by application of the Burg algorithm to irregularly sampled data"](http://resolver.tudelft.nl/uuid:870559f7-f1e9-4968-83da-edd19485eaaf). _IEEE Transactions on Instrumentation and Measurement_. **51** (6): 1289. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[2002ITIM...51.1289B](https://ui.adsabs.harvard.edu/abs/2002ITIM...51.1289B). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1109/TIM.2002.808031](https://doi.org/10.1109%2FTIM.2002.808031). [Archived](https://web.archive.org/web/20230416160911/https://repository.tudelft.nl/islandora/object/uuid:870559f7-f1e9-4968-83da-edd19485eaaf?collection=research) from the original on 2023-04-16. Retrieved 2019-12-11.
  23. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-23)** ["Fit Autoregressive Models to Time Series"](http://finzi.psych.upenn.edu/R/library/stats/html/ar.html) [Archived](https://web.archive.org/web/20160128234632/http://finzi.psych.upenn.edu/R/library/stats/html/ar.html) 2016-01-28 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine") (in R)
  24. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-:0_24-0)** Stoffer, David; Poison, Nicky (2023-01-09). ["astsa: Applied Statistical Time Series Analysis"](https://cran.r-project.org/web/packages/astsa/). Retrieved 2023-08-20.
  25. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-25)** ["Econometrics Toolbox"](https://www.mathworks.com/products/econometrics.html). _www.mathworks.com_. [Archived](https://web.archive.org/web/20230416160907/https://www.mathworks.com/products/econometrics.html) from the original on 2023-04-16. Retrieved 2022-02-16.
  26. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-26)** ["System Identification Toolbox"](https://www.mathworks.com/products/sysid.html). _www.mathworks.com_. [Archived](https://web.archive.org/web/20220216063519/https://www.mathworks.com/products/sysid.html) from the original on 2022-02-16. Retrieved 2022-02-16.
  27. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-27)** ["Autoregressive Model - MATLAB & Simulink"](https://www.mathworks.com/help/econ/autoregressive-model.html). _www.mathworks.com_. [Archived](https://web.archive.org/web/20220216063648/https://www.mathworks.com/help/econ/autoregressive-model.html) from the original on 2022-02-16. Retrieved 2022-02-16.
  28. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-28)** ["The Time Series Analysis (TSA) toolbox for Octave and MATLAB"](http://pub.ist.ac.at/~schloegl/matlab/tsa/). _pub.ist.ac.at_. [Archived](https://web.archive.org/web/20120511144225/http://pub.ist.ac.at/~schloegl/matlab/tsa/) from the original on 2012-05-11. Retrieved 2012-04-03.
  29. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-29)** ["christophmark/bayesloop"](https://github.com/christophmark/bayesloop). December 7, 2021. [Archived](https://web.archive.org/web/20200928085417/https://github.com/christophmark/bayesloop) from the original on September 28, 2020. Retrieved September 4, 2018 – via GitHub.
  30. **[^](https://en.wikipedia.org/wiki/Autoregressive_model#cite_ref-30)** ["statsmodels.tsa.ar_model.AutoReg — statsmodels 0.12.2 documentation"](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ar_model.AutoReg.html). _www.statsmodels.org_. [Archived](https://web.archive.org/web/20210228123354/https://www.statsmodels.org/stable/generated/statsmodels.tsa.ar_model.AutoReg.html) from the original on 2021-02-28. Retrieved 2021-04-29.


## References
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=20 "Edit section: References")]
  * Mills, Terence C. (1990). [_Time Series Techniques for Economists_](https://archive.org/details/timeseriestechni0000mill). Cambridge University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [9780521343398](https://en.wikipedia.org/wiki/Special:BookSources/9780521343398 "Special:BookSources/9780521343398").
  * Percival, Donald B.; Walden, Andrew T. (1993). _Spectral Analysis for Physical Applications_. Cambridge University Press. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode \(identifier\)"):[1993sapa.book.....P](https://ui.adsabs.harvard.edu/abs/1993sapa.book.....P).
  * Pandit, Sudhakar M.; Wu, Shien-Ming (1983). _Time Series and System Analysis with Applications_. John Wiley & Sons.


## External links
[[edit](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&action=edit&section=21 "Edit section: External links")]
  * [AutoRegression Analysis (AR)](http://paulbourke.net/miscellaneous/ar/) by Paul Bourke
  * [Econometrics lecture (topic: Autoregressive models)](https://www.youtube.com/watch?v=b8yslhlIsA0&list=PLD15D38DC7AA3B737&index=8#t=34m25s) on [YouTube](https://en.wikipedia.org/wiki/YouTube_video_\(identifier\) "YouTube video \(identifier\)") by [Mark Thoma](https://en.wikipedia.org/wiki/Mark_Thoma "Mark Thoma")

  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Stochastic_processes "Template:Stochastic processes")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Stochastic_processes "Template talk:Stochastic processes")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Stochastic_processes "Special:EditPage/Template:Stochastic processes")

[Stochastic processes](https://en.wikipedia.org/wiki/Stochastic_process "Stochastic process")  |  
| --- |  
| [Discrete time](https://en.wikipedia.org/wiki/Discrete-time_stochastic_process "Discrete-time stochastic process")  | 
  * [Bernoulli process](https://en.wikipedia.org/wiki/Bernoulli_process "Bernoulli process")
  * [Branching process](https://en.wikipedia.org/wiki/Branching_process "Branching process")
  * [Chinese restaurant process](https://en.wikipedia.org/wiki/Chinese_restaurant_process "Chinese restaurant process")
  * [Galton–Watson process](https://en.wikipedia.org/wiki/Galton%E2%80%93Watson_process "Galton–Watson process")
  * [Independent and identically distributed random variables](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables "Independent and identically distributed random variables")
  * [Markov chain](https://en.wikipedia.org/wiki/Markov_chain "Markov chain")
  * [Moran process](https://en.wikipedia.org/wiki/Moran_process "Moran process")
  * [Random walk](https://en.wikipedia.org/wiki/Random_walk "Random walk")
    * [Loop-erased](https://en.wikipedia.org/wiki/Loop-erased_random_walk "Loop-erased random walk")
    * [Self-avoiding](https://en.wikipedia.org/wiki/Self-avoiding_walk "Self-avoiding walk")
    * [ Biased](https://en.wikipedia.org/wiki/Biased_random_walk_on_a_graph "Biased random walk on a graph")
    * [Maximal entropy](https://en.wikipedia.org/wiki/Maximal_entropy_random_walk "Maximal entropy random walk")

 |  
| [Continuous time](https://en.wikipedia.org/wiki/Continuous-time_stochastic_process "Continuous-time stochastic process")  | 
  * [Additive process](https://en.wikipedia.org/wiki/Additive_process "Additive process")
  * [Airy process](https://en.wikipedia.org/wiki/Airy_process "Airy process")
  * [Bessel process](https://en.wikipedia.org/wiki/Bessel_process "Bessel process")
  * [Birth–death process](https://en.wikipedia.org/wiki/Birth%E2%80%93death_process "Birth–death process")
    * [pure birth](https://en.wikipedia.org/wiki/Birth_process "Birth process")
  * [Brownian motion](https://en.wikipedia.org/wiki/Wiener_process "Wiener process")
    * [Bridge](https://en.wikipedia.org/wiki/Brownian_bridge "Brownian bridge")
    * [Dyson](https://en.wikipedia.org/wiki/Dyson_Brownian_motion "Dyson Brownian motion")
    * [Excursion](https://en.wikipedia.org/wiki/Brownian_excursion "Brownian excursion")
    * [Fractional](https://en.wikipedia.org/wiki/Fractional_Brownian_motion "Fractional Brownian motion")
    * [Geometric](https://en.wikipedia.org/wiki/Geometric_Brownian_motion "Geometric Brownian motion")
    * [Meander](https://en.wikipedia.org/wiki/Brownian_meander "Brownian meander")
  * [Cauchy process](https://en.wikipedia.org/wiki/Cauchy_process "Cauchy process")
  * [Contact process](https://en.wikipedia.org/wiki/Contact_process_\(mathematics\) "Contact process \(mathematics\)")
  * [Continuous-time random walk](https://en.wikipedia.org/wiki/Continuous-time_random_walk "Continuous-time random walk")
  * [Cox process](https://en.wikipedia.org/wiki/Cox_process "Cox process")
  * [Diffusion process](https://en.wikipedia.org/wiki/Diffusion_process "Diffusion process")
  * [Empirical process](https://en.wikipedia.org/wiki/Empirical_process "Empirical process")
  * [Feller process](https://en.wikipedia.org/wiki/Feller_process "Feller process")
  * [Fleming–Viot process](https://en.wikipedia.org/wiki/Fleming%E2%80%93Viot_process "Fleming–Viot process")
  * [Gamma process](https://en.wikipedia.org/wiki/Gamma_process "Gamma process")
  * [Geometric process](https://en.wikipedia.org/wiki/Geometric_process "Geometric process")
  * [Hawkes process](https://en.wikipedia.org/wiki/Hawkes_process "Hawkes process")
  * [Hunt process](https://en.wikipedia.org/wiki/Hunt_process "Hunt process")
  * [Interacting particle systems](https://en.wikipedia.org/wiki/Interacting_particle_system "Interacting particle system")
  * [Itô diffusion](https://en.wikipedia.org/wiki/It%C3%B4_diffusion "Itô diffusion")
  * [Itô process](https://en.wikipedia.org/wiki/It%C3%B4_process "Itô process")
  * [Jump diffusion](https://en.wikipedia.org/wiki/Jump_diffusion "Jump diffusion")
  * [Jump process](https://en.wikipedia.org/wiki/Jump_process "Jump process")
  * [Lévy process](https://en.wikipedia.org/wiki/L%C3%A9vy_process "Lévy process")
  * [Local time](https://en.wikipedia.org/wiki/Local_time_\(mathematics\) "Local time \(mathematics\)")
  * [Markov additive process](https://en.wikipedia.org/wiki/Markov_additive_process "Markov additive process")
  * [McKean–Vlasov process](https://en.wikipedia.org/wiki/McKean%E2%80%93Vlasov_process "McKean–Vlasov process")
  * [Ornstein–Uhlenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process "Ornstein–Uhlenbeck process")
  * [Poisson process](https://en.wikipedia.org/wiki/Poisson_point_process "Poisson point process")
    * [Compound](https://en.wikipedia.org/wiki/Compound_Poisson_process "Compound Poisson process")
    * [Non-homogeneous](https://en.wikipedia.org/wiki/Non-homogeneous_Poisson_process "Non-homogeneous Poisson process")
  * [Quasimartingale](https://en.wikipedia.org/wiki/Quasimartingale "Quasimartingale")
  * [Schramm–Loewner evolution](https://en.wikipedia.org/wiki/Schramm%E2%80%93Loewner_evolution "Schramm–Loewner evolution")
  * [Semimartingale](https://en.wikipedia.org/wiki/Semimartingale "Semimartingale")
  * [Sigma-martingale](https://en.wikipedia.org/wiki/Sigma-martingale "Sigma-martingale")
  * [Stable process](https://en.wikipedia.org/wiki/Stable_process "Stable process")
  * [Superprocess](https://en.wikipedia.org/wiki/Superprocess "Superprocess")
  * [Telegraph process](https://en.wikipedia.org/wiki/Telegraph_process "Telegraph process")
  * [Variance gamma process](https://en.wikipedia.org/wiki/Variance_gamma_process "Variance gamma process")
  * [Wiener process](https://en.wikipedia.org/wiki/Wiener_process "Wiener process")
  * [Wiener sausage](https://en.wikipedia.org/wiki/Wiener_sausage "Wiener sausage")

 |  
| Both  | 
  * [Branching process](https://en.wikipedia.org/wiki/Branching_process "Branching process")
  * [Gaussian process](https://en.wikipedia.org/wiki/Gaussian_process "Gaussian process")
  * [Hidden Markov model (HMM)](https://en.wikipedia.org/wiki/Hidden_Markov_model "Hidden Markov model")
  * [Markov process](https://en.wikipedia.org/wiki/Markov_process "Markov process")
  * [Martingale](https://en.wikipedia.org/wiki/Martingale_\(probability_theory\) "Martingale \(probability theory\)")
    * [Differences](https://en.wikipedia.org/wiki/Martingale_difference_sequence "Martingale difference sequence")
    * [Local](https://en.wikipedia.org/wiki/Local_martingale "Local martingale")
    * [Sub-](https://en.wikipedia.org/wiki/Submartingale "Submartingale")
    * [Super-](https://en.wikipedia.org/wiki/Supermartingale "Supermartingale")
  * [Random dynamical system](https://en.wikipedia.org/wiki/Random_dynamical_system "Random dynamical system")
  * [Regenerative process](https://en.wikipedia.org/wiki/Regenerative_process "Regenerative process")
  * [Renewal process](https://en.wikipedia.org/wiki/Renewal_process "Renewal process")
  * [Stochastic chains with memory of variable length](https://en.wikipedia.org/wiki/Stochastic_chains_with_memory_of_variable_length "Stochastic chains with memory of variable length")
  * [White noise](https://en.wikipedia.org/wiki/White_noise "White noise")

 |  
| Fields and other  | 
  * [Dirichlet process](https://en.wikipedia.org/wiki/Dirichlet_process "Dirichlet process")
  * [Gaussian random field](https://en.wikipedia.org/wiki/Gaussian_random_field "Gaussian random field")
  * [Gibbs measure](https://en.wikipedia.org/wiki/Gibbs_measure "Gibbs measure")
  * [Hopfield model](https://en.wikipedia.org/wiki/Hopfield_model "Hopfield model")
  * [Ising model](https://en.wikipedia.org/wiki/Ising_model "Ising model")
    * [Potts model](https://en.wikipedia.org/wiki/Potts_model "Potts model")
    * [Boolean network](https://en.wikipedia.org/wiki/Boolean_network "Boolean network")
  * [Markov random field](https://en.wikipedia.org/wiki/Markov_random_field "Markov random field")
  * [Percolation](https://en.wikipedia.org/wiki/Percolation_theory "Percolation theory")
  * [Pitman–Yor process](https://en.wikipedia.org/wiki/Pitman%E2%80%93Yor_process "Pitman–Yor process")
  * [Point process](https://en.wikipedia.org/wiki/Point_process "Point process")
    * [Cox](https://en.wikipedia.org/wiki/Point_process#Cox_point_process "Point process")
    * [Determinantal](https://en.wikipedia.org/wiki/Determinantal_point_process "Determinantal point process")
    * [Poisson](https://en.wikipedia.org/wiki/Poisson_point_process "Poisson point process")
  * [Random field](https://en.wikipedia.org/wiki/Random_field "Random field")
  * [Random graph](https://en.wikipedia.org/wiki/Random_graph "Random graph")

 |  
| [Time series models](https://en.wikipedia.org/wiki/Time_series "Time series")  | 
  * [Autoregressive conditional heteroskedasticity (ARCH) model](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity "Autoregressive conditional heteroskedasticity")
  * [Autoregressive integrated moving average (ARIMA) model](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average "Autoregressive integrated moving average")
  * Autoregressive (AR) model
  * [Autoregressive moving-average (ARMA) model](https://en.wikipedia.org/wiki/Autoregressive_moving-average_model "Autoregressive moving-average model")
  * [Generalized autoregressive conditional heteroskedasticity (GARCH) model](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity "Autoregressive conditional heteroskedasticity")
  * [Moving-average (MA) model](https://en.wikipedia.org/wiki/Moving-average_model "Moving-average model")

 |  
| [Financial models](https://en.wikipedia.org/wiki/Asset_pricing_model "Asset pricing model")  | 
  * [Binomial options pricing model](https://en.wikipedia.org/wiki/Binomial_options_pricing_model "Binomial options pricing model")
  * [Black–Derman–Toy](https://en.wikipedia.org/wiki/Black%E2%80%93Derman%E2%80%93Toy_model "Black–Derman–Toy model")
  * [Black–Karasinski](https://en.wikipedia.org/wiki/Black%E2%80%93Karasinski_model "Black–Karasinski model")
  * [Black–Scholes](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model "Black–Scholes model")
  * [Chan–Karolyi–Longstaff–Sanders (CKLS)](https://en.wikipedia.org/wiki/Chan%E2%80%93Karolyi%E2%80%93Longstaff%E2%80%93Sanders_process "Chan–Karolyi–Longstaff–Sanders process")
  * [Chen](https://en.wikipedia.org/wiki/Chen_model "Chen model")
  * [Constant elasticity of variance (CEV)](https://en.wikipedia.org/wiki/Constant_elasticity_of_variance_model "Constant elasticity of variance model")
  * [Cox–Ingersoll–Ross (CIR)](https://en.wikipedia.org/wiki/Cox%E2%80%93Ingersoll%E2%80%93Ross_model "Cox–Ingersoll–Ross model")
  * [Garman–Kohlhagen](https://en.wikipedia.org/wiki/Garman%E2%80%93Kohlhagen_model "Garman–Kohlhagen model")
  * [Heath–Jarrow–Morton (HJM)](https://en.wikipedia.org/wiki/Heath%E2%80%93Jarrow%E2%80%93Morton_framework "Heath–Jarrow–Morton framework")
  * [Heston](https://en.wikipedia.org/wiki/Heston_model "Heston model")
  * [Ho–Lee](https://en.wikipedia.org/wiki/Ho%E2%80%93Lee_model "Ho–Lee model")
  * [Hull–White](https://en.wikipedia.org/wiki/Hull%E2%80%93White_model "Hull–White model")
  * [Korn-Kreer-Lenssen](https://en.wikipedia.org/wiki/Korn%E2%80%93Kreer%E2%80%93Lenssen_model "Korn–Kreer–Lenssen model")
  * [LIBOR market](https://en.wikipedia.org/wiki/LIBOR_market_model "LIBOR market model")
  * [Rendleman–Bartter](https://en.wikipedia.org/wiki/Rendleman%E2%80%93Bartter_model "Rendleman–Bartter model")
  * [SABR volatility](https://en.wikipedia.org/wiki/SABR_volatility_model "SABR volatility model")
  * [Vašíček](https://en.wikipedia.org/wiki/Vasicek_model "Vasicek model")
  * [Wilkie](https://en.wikipedia.org/wiki/Wilkie_investment_model "Wilkie investment model")

 |  
| [Actuarial models](https://en.wikipedia.org/wiki/Actuarial_mathematics "Actuarial mathematics")  | 
  * [Bühlmann](https://en.wikipedia.org/wiki/B%C3%BChlmann_model "Bühlmann model")
  * [Cramér–Lundberg](https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Lundberg_model "Cramér–Lundberg model")
  * [Risk process](https://en.wikipedia.org/wiki/Risk_process "Risk process")
  * [Sparre–Anderson](https://en.wikipedia.org/wiki/Sparre%E2%80%93Anderson_model "Sparre–Anderson model")

 |  
| [Queueing models](https://en.wikipedia.org/wiki/Queueing_model "Queueing model")  | 
  * [Bulk](https://en.wikipedia.org/wiki/Bulk_queue "Bulk queue")
  * [Fluid](https://en.wikipedia.org/wiki/Fluid_queue "Fluid queue")
  * [Generalized queueing network](https://en.wikipedia.org/wiki/G-network "G-network")
  * [M/G/1](https://en.wikipedia.org/wiki/M/G/1_queue "M/G/1 queue")
  * [M/M/1](https://en.wikipedia.org/wiki/M/M/1_queue "M/M/1 queue")
  * [M/M/c](https://en.wikipedia.org/wiki/M/M/c_queue "M/M/c queue")

 |  
| Properties  | 
  * [Càdlàg paths](https://en.wikipedia.org/wiki/C%C3%A0dl%C3%A0g "Càdlàg")
  * [Continuous](https://en.wikipedia.org/wiki/Continuous_stochastic_process "Continuous stochastic process")
  * [Continuous paths](https://en.wikipedia.org/wiki/Sample-continuous_process "Sample-continuous process")
  * [Ergodic](https://en.wikipedia.org/wiki/Ergodicity "Ergodicity")
  * [Exchangeable](https://en.wikipedia.org/wiki/Exchangeable_random_variables "Exchangeable random variables")
  * [Feller-continuous](https://en.wikipedia.org/wiki/Feller-continuous_process "Feller-continuous process")
  * [Gauss–Markov](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_process "Gauss–Markov process")
  * [Markov](https://en.wikipedia.org/wiki/Markov_property "Markov property")
  * [Mixing](https://en.wikipedia.org/wiki/Mixing_\(mathematics\) "Mixing \(mathematics\)")
  * [Piecewise-deterministic](https://en.wikipedia.org/wiki/Piecewise-deterministic_Markov_process "Piecewise-deterministic Markov process")
  * [Predictable](https://en.wikipedia.org/wiki/Predictable_process "Predictable process")
  * [Progressively measurable](https://en.wikipedia.org/wiki/Progressively_measurable_process "Progressively measurable process")
  * [Self-similar](https://en.wikipedia.org/wiki/Self-similar_process "Self-similar process")
  * [Stationary](https://en.wikipedia.org/wiki/Stationary_process "Stationary process")
  * [Time-reversible](https://en.wikipedia.org/wiki/Time_reversibility "Time reversibility")

 |  
| Limit theorems  | 
  * [Central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem "Central limit theorem")
  * [Donsker's theorem](https://en.wikipedia.org/wiki/Donsker%27s_theorem "Donsker's theorem")
  * [Doob's martingale convergence theorems](https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems "Doob's martingale convergence theorems")
  * [Ergodic theorem](https://en.wikipedia.org/wiki/Ergodic_theory "Ergodic theory")
  * [Fisher–Tippett–Gnedenko theorem](https://en.wikipedia.org/wiki/Fisher%E2%80%93Tippett%E2%80%93Gnedenko_theorem "Fisher–Tippett–Gnedenko theorem")
  * [Large deviation principle](https://en.wikipedia.org/wiki/Large_deviation_principle "Large deviation principle")
  * [Law of large numbers (weak/strong)](https://en.wikipedia.org/wiki/Law_of_large_numbers "Law of large numbers")
  * [Law of the iterated logarithm](https://en.wikipedia.org/wiki/Law_of_the_iterated_logarithm "Law of the iterated logarithm")
  * [Maximal ergodic theorem](https://en.wikipedia.org/wiki/Maximal_ergodic_theorem "Maximal ergodic theorem")
  * [Sanov's theorem](https://en.wikipedia.org/wiki/Sanov%27s_theorem "Sanov's theorem")
  * [Zero–one laws](https://en.wikipedia.org/wiki/Zero%E2%80%93one_law "Zero–one law") ([Blumenthal](https://en.wikipedia.org/wiki/Blumenthal%27s_zero%E2%80%93one_law "Blumenthal's zero–one law"), [Borel–Cantelli](https://en.wikipedia.org/wiki/Borel%E2%80%93Cantelli_lemma "Borel–Cantelli lemma"), [Engelbert–Schmidt](https://en.wikipedia.org/wiki/Engelbert%E2%80%93Schmidt_zero%E2%80%93one_law "Engelbert–Schmidt zero–one law"), [Hewitt–Savage](https://en.wikipedia.org/wiki/Hewitt%E2%80%93Savage_zero%E2%80%93one_law "Hewitt–Savage zero–one law"), [ Kolmogorov](https://en.wikipedia.org/wiki/Kolmogorov%27s_zero%E2%80%93one_law "Kolmogorov's zero–one law"), [Lévy](https://en.wikipedia.org/wiki/L%C3%A9vy%27s_zero%E2%80%93one_law "Lévy's zero–one law"))

 |  
| [Inequalities](https://en.wikipedia.org/wiki/List_of_inequalities#Probability_theory_and_statistics "List of inequalities")  | 
  * [Burkholder–Davis–Gundy](https://en.wikipedia.org/wiki/Burkholder%E2%80%93Davis%E2%80%93Gundy_inequalities "Burkholder–Davis–Gundy inequalities")
  * [Doob's martingale](https://en.wikipedia.org/wiki/Doob%27s_martingale_inequality "Doob's martingale inequality")
  * [Doob's upcrossing](https://en.wikipedia.org/wiki/Doob%27s_upcrossing_inequality "Doob's upcrossing inequality")
  * [Kunita–Watanabe](https://en.wikipedia.org/wiki/Kunita%E2%80%93Watanabe_inequality "Kunita–Watanabe inequality")
  * [Marcinkiewicz–Zygmund](https://en.wikipedia.org/wiki/Marcinkiewicz%E2%80%93Zygmund_inequality "Marcinkiewicz–Zygmund inequality")

 |  
| Tools  | 
  * [Cameron–Martin theorem](https://en.wikipedia.org/wiki/Cameron%E2%80%93Martin_theorem "Cameron–Martin theorem")
  * [Convergence of random variables](https://en.wikipedia.org/wiki/Convergence_of_random_variables "Convergence of random variables")
  * [Doléans-Dade exponential](https://en.wikipedia.org/wiki/Dol%C3%A9ans-Dade_exponential "Doléans-Dade exponential")
  * [Doob decomposition theorem](https://en.wikipedia.org/wiki/Doob_decomposition_theorem "Doob decomposition theorem")
  * [Doob–Meyer decomposition theorem](https://en.wikipedia.org/wiki/Doob%E2%80%93Meyer_decomposition_theorem "Doob–Meyer decomposition theorem")
  * [Doob's optional stopping theorem](https://en.wikipedia.org/wiki/Doob%27s_optional_stopping_theorem "Doob's optional stopping theorem")
  * [Dynkin's formula](https://en.wikipedia.org/wiki/Dynkin%27s_formula "Dynkin's formula")
  * [Feynman–Kac formula](https://en.wikipedia.org/wiki/Feynman%E2%80%93Kac_formula "Feynman–Kac formula")
  * [Filtration](https://en.wikipedia.org/wiki/Filtration_\(probability_theory\) "Filtration \(probability theory\)")
  * [Girsanov theorem](https://en.wikipedia.org/wiki/Girsanov_theorem "Girsanov theorem")
  * [Infinitesimal generator](https://en.wikipedia.org/wiki/Infinitesimal_generator_\(stochastic_processes\) "Infinitesimal generator \(stochastic processes\)")
  * [Itô integral](https://en.wikipedia.org/wiki/It%C3%B4_integral "Itô integral")
  * [Itô's lemma](https://en.wikipedia.org/wiki/It%C3%B4%27s_lemma "Itô's lemma")
  * [Kolmogorov continuity theorem](https://en.wikipedia.org/wiki/Kolmogorov_continuity_theorem "Kolmogorov continuity theorem")
  * [Kolmogorov extension theorem](https://en.wikipedia.org/wiki/Kolmogorov_extension_theorem "Kolmogorov extension theorem")
  * [Kosambi–Karhunen–Loève theorem](https://en.wikipedia.org/wiki/Kosambi%E2%80%93Karhunen%E2%80%93Lo%C3%A8ve_theorem "Kosambi–Karhunen–Loève theorem")
  * [Lévy–Prokhorov metric](https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Prokhorov_metric "Lévy–Prokhorov metric")
  * [Malliavin calculus](https://en.wikipedia.org/wiki/Malliavin_calculus "Malliavin calculus")
  * [Martingale representation theorem](https://en.wikipedia.org/wiki/Martingale_representation_theorem "Martingale representation theorem")
  * [Optional stopping theorem](https://en.wikipedia.org/wiki/Optional_stopping_theorem "Optional stopping theorem")
  * [Prokhorov's theorem](https://en.wikipedia.org/wiki/Prokhorov%27s_theorem "Prokhorov's theorem")
  * [Quadratic variation](https://en.wikipedia.org/wiki/Quadratic_variation "Quadratic variation")
  * [Reflection principle](https://en.wikipedia.org/wiki/Reflection_principle_\(Wiener_process\) "Reflection principle \(Wiener process\)")
  * [Skorokhod integral](https://en.wikipedia.org/wiki/Skorokhod_integral "Skorokhod integral")
  * [Skorokhod's representation theorem](https://en.wikipedia.org/wiki/Skorokhod%27s_representation_theorem "Skorokhod's representation theorem")
  * [Skorokhod space](https://en.wikipedia.org/wiki/Skorokhod_space "Skorokhod space")
  * [Snell envelope](https://en.wikipedia.org/wiki/Snell_envelope "Snell envelope")
  * [Stochastic differential equation](https://en.wikipedia.org/wiki/Stochastic_differential_equation "Stochastic differential equation")
    * [Tanaka](https://en.wikipedia.org/wiki/Tanaka_equation "Tanaka equation")
  * [Stopping time](https://en.wikipedia.org/wiki/Stopping_time "Stopping time")
  * [Stratonovich integral](https://en.wikipedia.org/wiki/Stratonovich_integral "Stratonovich integral")
  * [Uniform integrability](https://en.wikipedia.org/wiki/Uniform_integrability "Uniform integrability")
  * [Usual hypotheses](https://en.wikipedia.org/wiki/Usual_hypotheses "Usual hypotheses")
  * Wiener space 
    * [Classical](https://en.wikipedia.org/wiki/Classical_Wiener_space "Classical Wiener space")
    * [Abstract](https://en.wikipedia.org/wiki/Abstract_Wiener_space "Abstract Wiener space")

 |  
| Disciplines  | 
  * [Actuarial mathematics](https://en.wikipedia.org/wiki/Actuarial_mathematics "Actuarial mathematics")
  * [Control theory](https://en.wikipedia.org/wiki/Stochastic_control "Stochastic control")
  * [Econometrics](https://en.wikipedia.org/wiki/Econometrics "Econometrics")
  * [Ergodic theory](https://en.wikipedia.org/wiki/Ergodic_theory "Ergodic theory")
  * [Extreme value theory (EVT)](https://en.wikipedia.org/wiki/Extreme_value_theory "Extreme value theory")
  * [Large deviations theory](https://en.wikipedia.org/wiki/Large_deviations_theory "Large deviations theory")
  * [Mathematical finance](https://en.wikipedia.org/wiki/Mathematical_finance "Mathematical finance")
  * [Mathematical statistics](https://en.wikipedia.org/wiki/Mathematical_statistics "Mathematical statistics")
  * [Probability theory](https://en.wikipedia.org/wiki/Probability_theory "Probability theory")
  * [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory "Queueing theory")
  * [Renewal theory](https://en.wikipedia.org/wiki/Renewal_theory "Renewal theory")
  * [Ruin theory](https://en.wikipedia.org/wiki/Ruin_theory "Ruin theory")
  * [Signal processing](https://en.wikipedia.org/wiki/Signal_processing "Signal processing")
  * [Statistics](https://en.wikipedia.org/wiki/Statistics "Statistics")
  * [Stochastic analysis](https://en.wikipedia.org/wiki/Stochastic_analysis "Stochastic analysis")
  * [Time series analysis](https://en.wikipedia.org/wiki/Time_series_analysis "Time series analysis")
  * [Machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning")

 |  
| 
  * [List of topics](https://en.wikipedia.org/wiki/List_of_stochastic_processes_topics "List of stochastic processes topics")
  * [Category](https://en.wikipedia.org/wiki/Category:Stochastic_processes "Category:Stochastic processes")

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
  * Autoregression
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
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Autoregressive_model&oldid=1358105099](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&oldid=1358105099)"
[Categories](https://en.wikipedia.org/wiki/Help:Category "Help:Category"): 
  * [Autocorrelation](https://en.wikipedia.org/wiki/Category:Autocorrelation "Category:Autocorrelation")
  * [Signal processing](https://en.wikipedia.org/wiki/Category:Signal_processing "Category:Signal processing")


Hidden categories: 
  * [Webarchive template wayback links](https://en.wikipedia.org/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
  * [Wikipedia articles needing page number citations from March 2011](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_page_number_citations_from_March_2011 "Category:Wikipedia articles needing page number citations from March 2011")
  * [Articles with short description](https://en.wikipedia.org/wiki/Category:Articles_with_short_description "Category:Articles with short description")
  * [Short description matches Wikidata](https://en.wikipedia.org/wiki/Category:Short_description_matches_Wikidata "Category:Short description matches Wikidata")
  * [Articles lacking in-text citations from March 2011](https://en.wikipedia.org/wiki/Category:Articles_lacking_in-text_citations_from_March_2011 "Category:Articles lacking in-text citations from March 2011")
  * [All articles lacking in-text citations](https://en.wikipedia.org/wiki/Category:All_articles_lacking_in-text_citations "Category:All articles lacking in-text citations")
  * [All articles with unsourced statements](https://en.wikipedia.org/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
  * [Articles with unsourced statements from October 2011](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_October_2011 "Category:Articles with unsourced statements from October 2011")
  * [Articles with unsourced statements from July 2022](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_July_2022 "Category:Articles with unsourced statements from July 2022")
  * [Wikipedia articles needing clarification from July 2020](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_July_2020 "Category:Wikipedia articles needing clarification from July 2020")


  * This page was last edited on 6 June 2026, at 16:07 (UTC).
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
  * [Mobile view](https://en.wikipedia.org/w/index.php?title=Autoregressive_model&mobileaction=toggle_view_mobile)


  * [![Wikimedia Foundation](https://en.wikipedia.org/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
  * [![Powered by MediaWiki](https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)


Search
Search
Toggle the table of contents
Autoregressive model
[](https://en.wikipedia.org/wiki/Autoregressive_model) [](https://en.wikipedia.org/wiki/Autoregressive_model) [](https://en.wikipedia.org/wiki/Autoregressive_model) [](https://en.wikipedia.org/wiki/Autoregressive_model) [](https://en.wikipedia.org/wiki/Autoregressive_model) [](https://en.wikipedia.org/wiki/Autoregressive_model) [](https://en.wikipedia.org/wiki/Autoregressive_model)
20 languages [Add topic ](https://en.wikipedia.org/wiki/Autoregressive_model)
  *[v]: View this template
  *[t]: Discuss this template
  *[e]: Edit this template
