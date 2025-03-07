STREAMLITAPP
<a href="https://appapp-ndzyc5va4gcol2vj2pw4nx.streamlit.app/"> Gerenciamento de Despesas</a>

O StreamLitApp é uma aplicação web interativa construída com Streamlit, projetada para facilitar a análise exploratória de dados. Composto por 4 páginas distintas, ele permite que usuários explorem um conjunto de dados (dados.csv) de maneira intuitiva e dinâmica, através de visualizações e ferramentas interativas.

Estrutura do Projeto:
app.py: O arquivo principal que orquestra a aplicação Streamlit, define a estrutura das páginas e implementa a lógica de análise de dados.
dados.csv: O conjunto de dados que será analisado pela aplicação.
requirements.txt: Um arquivo que lista as dependências Python necessárias para executar o aplicativo, garantindo a reprodução do ambiente.
pages/: Um diretório que contém os scripts Python para cada uma das 4 páginas da aplicação.
.streamlit/: Um diretório de configuração do Streamlit, que pode conter configurações adicionais para a aplicação.
Etapas e Desenvolvimento Web:

Estrutura da Aplicação:
O arquivo app.py serve como ponto de entrada, onde a estrutura geral da aplicação é definida. Utilizando o Streamlit, o desenvolvedor cria um layout intuitivo com navegação entre as 4 páginas.
A biblioteca Streamlit simplifica o desenvolvimento web, permitindo que o desenvolvedor crie interfaces interativas usando apenas código Python, sem a necessidade de conhecimento extenso em HTML, CSS ou JavaScript.

Páginas Individuais (pages/):
Cada arquivo dentro do diretório pages/ representa uma página distinta da aplicação.
Utilizando as funcionalidades do Streamlit, cada página é construída com:
Visualizações: Gráficos interativos (histogramas, gráficos de dispersão, etc.) para explorar a distribuição e relações entre as variáveis do conjunto de dados.
Widgets Interativos: Controles deslizantes, seletores e caixas de texto que permitem aos usuários filtrar, selecionar e manipular os dados e visualizações.
Tabelas e Resumos: Exibição de dados tabulares e estatísticas descritivas para fornecer informações detalhadas sobre o conjunto de dados.
Análise Exploratória de Dados (EDA):

Em cada página, o desenvolvedor implementa técnicas de EDA utilizando bibliotecas Python como Pandas e Matplotlib/Seaborn.
O Streamlit permite a integração perfeita dessas bibliotecas, possibilitando a criação de visualizações interativas que auxiliam na identificação de padrões, tendências e outliers nos dados.
Interatividade e Dinamismo:
O Streamlit permite que a aplicação seja altamente interativa, com atualizações em tempo real das visualizações e resultados à medida que os usuários interagem com os widgets.
Essa interatividade facilita a exploração dos dados, permitindo que os usuários testem diferentes hipóteses e obtenham insights de forma rápida e eficiente.

Funcionalidades Possíveis de Cada Página:
Página 1 (Visão Geral): Estatísticas descritivas do conjunto de dados, resumo das variáveis e visualizações gerais.
Página 2 (Distribuição das Variáveis): Histogramas e boxplots para visualizar a distribuição de cada variável.
Página 3 (Relação entre Variáveis): Gráficos de dispersão e mapas de calor para explorar a correlação entre as variáveis.
Página 4 (Filtragem e Seleção): Ferramentas interativas para filtrar e selecionar subconjuntos de dados com base em critérios específicos.
Em resumo, esse aplicativo Streamlit oferece uma forma muito eficaz de realizar a EDA, de maneira totalmente online, bastando apenas abrir o navegador, e fornece uma interface completa e interativa para que o usuário final possa interagir com os dados desejados.
