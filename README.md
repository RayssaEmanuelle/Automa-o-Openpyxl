README: Automação para Criar e Modificar Planilhas com Openpyxl 📊
Descrição do Projeto
Este projeto utiliza a biblioteca Openpyxl para automatizar a criação de planilhas no formato Excel (.xlsx). Ele permite criar uma nova planilha, adicionar dados de forma organizada e salvar essas informações para uso futuro. A automação pode ser usada para registrar e atualizar informações como cursos, eventos, listas de tarefas, ou qualquer tipo de dados tabulares.

Recursos
Criação de Planilhas:

Geração de um arquivo Excel vazio com várias abas.
Configuração personalizada do nome da planilha e do caminho do arquivo.
Inserção de Dados:

Adição de informações em formato de tabela, com suporte a vários tipos de dados (texto, datas, números).
Uso de métodos simples como append() para adicionar novas linhas de dados.
Facilidade de Modificação:

Alteração de dados existentes na planilha.
Adição de novas planilhas e páginas conforme necessário.
Salvamento:

Salvamento automático do arquivo Excel com o nome e formato desejado.
Pré-Requisitos
Python 3.8+
Biblioteca Openpyxl
Instalação:
bash
Copiar código
pip install openpyxl
Como Usar
Clonar o Repositório (se aplicável):
Se estiver usando um repositório do GitHub, clone o projeto para sua máquina local:

bash
Copiar código
git clone <url-do-repositorio>
cd <nome-do-diretorio>
Configurar e Executar o Script:

Abra o arquivo main.py (ou qualquer nome do arquivo Python do seu projeto).
O script já vem configurado para criar uma planilha de cursos. Para adicionar ou modificar os dados, basta editar as informações dentro do código.
Execute o script para gerar a planilha com os dados configurados.
bash
Copiar código
python main.py
Personalização de Dados:

Para alterar ou adicionar mais cursos, modifique os itens dentro da função append(). Cada entrada de curso pode ser modificada conforme a necessidade.
Exemplo do Código
python
Copiar código
import openpyxl

# Criação do arquivo Excel
book = openpyxl.Workbook()

# Exibição das planilhas criadas até agora
print(book.sheetnames)

# Criação de uma nova aba chamada 'Cursos'
book.create_sheet('Cursos')
Cursos_page = book['Cursos']

# Adicionando cursos e suas datas
Cursos_page.append(['CURSO DE AURICULOTERAPIA', '03/11'])
Cursos_page.append(['CURSO DE HIDROLIPOCLASIA NÃO ASPIRATIIVA', '03/11'])
Cursos_page.append(['CURSO DE MICROAGULHAMENTO: FACIAL E CORPORAL', '16/11'])
Cursos_page.append(['CURSO DE LIBERAÇÃO MIOFASCIAL: MANUAL E INSTRUMENTAL', '16/11'])
Cursos_page.append(['CURSO DE DRENAGEM LINFÁTICA INJETADA', '16/11'])
Cursos_page.append(['CURSO DE LIMPEZA DE PELE + DERMAPLANING E HIDRAGLOSS', '17/11'])
Cursos_page.append(['CURSO DE TOXINA BOTULINICA', '17/11'])
Cursos_page.append(['CURSO DE BANDAGEM NEUROMUSCULAR', '17/11'])
Cursos_page.append(['CURSO DE CINESIOTERAPIA E BIOMECÂNICA', '23/11'])
Cursos_page.append(['CURSO DE DRY NEELING ASSOCIADO A ELETROTERAPIA', '23/11'])
Cursos_page.append(['CURSO DE LIPOENZIMÁTICA DE PAPADA + SKINBOOSTER FACIAL + INTRADERMOTERAPIA CAPILAR', '23/11'])
Cursos_page.append(['CURSO DE DRENAGEM LINFATICA + MASSAGEM MODELADORA + ULTRASSOM ESTETICO', '24/11'])
Cursos_page.append(['CURSO DE PILATES APLICADO A PESSOA IDOSA', '24/11'])
Cursos_page.append(['CURSO DE LASER TAPING NA GESTAÇÃO E NO PÓS-OPERATÓRIO', '24/11'])
Cursos_page.append(['CURSO DE AVALIAÇÃO FISIOTERAPÊUTICA', '30/11'])
Cursos_page.append(['CURSO DE PROCEDIMENTO ESTETICO INJETÁVEL PARA MICROVASOS - PEIM', '30/11'])
Cursos_page.append(['CURSO DE JATO DE PLASMA', '30/11'])

# Salvando o arquivo
book.save("Cursos.xlsx")
Casos de Uso
Gestão de Cursos:
Este script pode ser usado para registrar cursos, workshops e eventos em uma planilha de fácil acesso.

Gestão de Tarefas:
Utilize a mesma estrutura para criar listas de tarefas, compromissos ou qualquer outro tipo de controle.

Relatórios Automatizados:
Gere relatórios automatizados com base em dados que podem ser extraídos de sistemas e armazenados em planilhas Excel.

Contribuição
Se desejar contribuir, siga os seguintes passos:

Faça um fork do repositório.
Crie um branch para sua feature:
bash
Copiar código
git checkout -b minha-feature
Faça as alterações e adicione o commit:
bash
Copiar código
git commit -m "Adiciona novo curso à lista"
Envie para o repositório principal:
bash
Copiar código
git push origin minha-feature
