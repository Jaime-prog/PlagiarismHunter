# 🕵🏻‍♂️Plagiarism Hunter (tool for plagiarism detector)🕵🏻‍♂️

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un clasificador para la detección de plagio en código fuente escrito en Java.

La detección de plagio en software es un desafío crítico tanto en el ámbito académico como en el empresarial. Este proyecto busca abordar este problema utilizando técnicas avanzadas de análisis de código y algoritmos de aprendizaje supervisado utilizados para problemas de clasificación.

### Algoritmos del Proyecto

- **Árboles de Sintaxis Abstracta (AST):** Estructura de datos en forma de árbol que representa la sintaxis abstracta de un lenguaje de programación.

**Modelos de Machine Learning:**

- **Random Forest:** Algoritmo de aprendizaje supervisado que utiliza múltiples árboles de decisión, combinando sus resultados para mejorar la precisión de las predicciones.

- **XGBoost:** Algoritmo de aprendizaje automático altamente eficiente que se utiliza para tareas de clasificación. Utiliza árboles de decisión y boosting, una técnica de ensamblaje que combina predicciones de varios modelos más simples para formar un modelo más preciso.

- **Gradient Boosting Decision Tree (GBDT):** Es una técnica de ensamble que utiliza múltiples árboles de decisión entrenados secuencialmente. Cada nuevo árbol se construye para corregir los errores cometidos por los árboles anteriores, optimizando gradualmente el rendimiento del modelo.

## Referencias

[1] D. Rattan, A. Bansal, y R. Sabharwal, "Software clone detection: A systematic review", Information and Software Technology, vol. 55, no. 11, pp. 1165-1199, Nov. 2013. doi: 10.1016/j.infsof.2013.03.004.

[2] J. Zhao, H. Huo, y Y. Sun, "Research on Code Plagiarism Detection Model Based on Random Forest and Gradient Boosting Decision Tree", Proceedings of the ACM Turing Celebration Conference - China, pp. 74-80, May 2019. doi: 10.1145/3335656.3335692.

[3] S. Narayanan y S. S, "AST-Based Code Plagiarism Detection Algorithm", International Journal of Advanced Computer Science and Applications, vol. 12, no. 4, pp. 1-10, Apr. 2021. doi: 10.14569/IJACSA.2021.0120401.

[4] C. K. Roy, J. R. Cordy, y R. Koschke, "Comparison and evaluation of code clone detection techniques and tools: A qualitative approach", Science of Computer Programming, vol. 74, no. 7, pp. 470-495, May 2009. doi: 10.1016/j.scico.2009.02.007.

[5] A. Mezzetti, A. Besenov, J. Winter, J. Köhl, y N. Wütherich, "ConPlag: a Dataset of Programming Contest Plagiarism in Java", Zenodo, 2022. https://zenodo.org/record/7332491#.ZGuFmtLMKXK.

[6] A. Mezzetti, D. Blichmann, L. Bossuet, M. Buratti, T. Coppetti, L. Dalla Costa, M. Dumitrescu, V. G. Gomes, J. H. Harting, P. Kundig, G. Lechner, A. Lupetti, R. Mazzariol, S. Meuli, T. Schmid, L. Thies, y M. Uhlmann, "FIRE14 Detection of SOurce COde Re-use, Zenodo, 2022. https://zenodo.org/record/7357805#.ZGuLetLMKXJ.

[7] T. Chen and C. Guestrin, “XGBoost: a Scalable Tree Boosting System”, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining - KDD ’16, pp. 785–794, 2016, doi: https://doi.org/10.1145/2939672.2939785.
