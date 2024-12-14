# NLP Semantic Clustering and Labeling

Este proyecto aborda la **clasificación y codificación de respuestas a preguntas abiertas** utilizando técnicas de procesamiento de lenguaje natural (NLP). El objetivo principal es optimizar el proceso de categorización y etiquetado mediante métodos automatizados que mejoren la eficiencia y la calidad de los resultados.

## 🔍 Problema de Investigación
El Instituto Nacional de Estadística e Informática (INEI) enfrenta retos al clasificar y codificar variables de forma manual, lo que consume tiempo, recursos humanos y puede impactar en la calidad de los resultados.

**Pregunta de Investigación:**  
¿Cómo optimizar el proceso de codificación y clasificación de la variable asociada a la opinión sobre los principales problemas del país, empleando datos del módulo de gobernabilidad de la ENAHO (2019-2023)?

## 🎯 Objetivos

### Objetivo General
Evaluar la viabilidad de los métodos de NLP para la codificación y etiquetado de respuestas abiertas en preguntas del módulo de gobernabilidad de la ENAHO.

### Objetivos Específicos
1. Explorar y comparar diferentes modelos de clusterización semántica basados en reducción de dimensionalidad y escalamiento.
2. Evaluar modelos de lenguaje (LLM) para codificar y etiquetar respuestas abiertas.
3. Diseñar un pipeline automatizado para la codificación y etiquetado de respuestas abiertas.

## 📚 Metodología

### Fuente de Datos
Los datos provienen de la **Encuesta Nacional de Hogares (ENAHO)** del INEI (2019-2023), específicamente de la pregunta 2 del módulo de gobernabilidad.

### Estrategia
1. **Limpieza de Datos:** Preprocesamiento de textos.
2. **Clusterización Semántica:** Reducción de dimensionalidad y agrupamiento usando embeddings y algoritmos como DBSCAN y HDBSCAN.
3. **Generación de Tópicos:** Identificación de categorías representativas.
4. **Pipeline Automatizado:** Proceso integrado para codificar y etiquetar respuestas.

### Herramientas
- **Embeddings:** MiniLM, FastText, y BERT.
- **Reducción de Dimensionalidad:** PCA y UMAP.
- **Clusterización:** HDBSCAN, OPTICS, DBSCAN y KMeans.
- **Evaluación de Modelos:** Métricas como Silhouette Score, Davies-Bouldin Index, y Calinski-Harabasz Index.

## 🔬 Resultados
- Implementación de un pipeline automatizado que genera categorías de respuestas abiertas.
- Evaluación comparativa entre modelos como SVM, T5, y LLaMA:
  - **SVM:** Gran F1-Score en la clasificación.
  - **T5 y LLaMA:** Generación de etiquetas más representativas para tópicos complejos.

### Ejemplo de Clusters (SVM - Año 2019)
| Cluster   | Categoría            |
|-----------|----------------------|
| 1         | No sabe             |
| 2         | Violencia           |
| 3         | Servicios básicos   |
| 4         | Abuso sexual        |
| 5         | Crisis y corrupción |

## 📈 Limitaciones y Extensiones

### Limitaciones
- Calidad de los datos iniciales.
- Escasez de datos etiquetados.
- Recursos computacionales limitados (GPU/TPU).

### Extensiones Futuras
- Explorar modelos más específicos para generación de etiquetas.
- Investigar el uso de técnicas de generación de datos sintéticos.

## 🚀 Cómo Ejecutar el Proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Diego-Vasquez/nlp-semantic-clustering-and-labeling.git
   cd nlp-semantic-clustering-and-labeling


## Autores
- Carlos Cahuama
- Diego Vásquez
- Mauricio Condori
- Probo Camayo