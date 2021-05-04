### Multi-Dimensional Performance Impact Analysis of Software Updates in Software Development Lifecycle

Chidera Biringa - University of Massachusetts Thesis in requirements for M.S. Computer Science Degree

#### Abstract
Software Development Life Cycle refers to the methodology used in developing and deploying software products. Software development teams often adopt an agile testing framework used in the quick test and integration of software features into the codebase. There are several established automated software testing suites, and they usually focus on unit, integration, system, and interface testing. However, software updates such as new security features have the potential to diminish user experience. 

In this thesis, we propose a novel automated user experience testing methodology. This methodology learns how code changes impact the time unit and system tests and extrapolates user experience changes based on this information. Our tool provides software teams immediate user experience feedback and could potentially integrate into existing continuous integration pipelines. We construct a stylometry feature set from lexical, layout, and syntactic characteristics of the source code. Using Abstract Syntax Tree-Based Embeddings, we can calculate the approximate semantic distance to feed into a machine learning algorithm. In our experiments, we use several regression methods to estimate the time impact of software updates. Our open-source tool achieved a 3.7\% and 0.8\% cross-validation mean absolute error rate with a random forest regressor on our first and second experiments. 

#### Publication
Chidera Biringa, Gokhan Kul. 2021. User Experience Testing through Multi-Dimensional Performance Impact Analysis. In Proceedings of the IEEE/ACM International Conference on Automation of Software Test.
