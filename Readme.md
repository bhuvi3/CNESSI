# CNESSI: Citation Network with Enhanced Structural and Semantic Information.

The is a research project in Scientometry, aimed at qualitative improvement of Digital Libraries and indexing tools like Google Scholar. The lack of semantic and structural information in the citation networks is restricting us to extract insights based on the quantitative knowledge present in the research documents. With the help of such quantitative knowledge embedded in the citation network, it is possible to connect and track the growth the knowledge in specific fields of study and extract vast number of useful insights.

Through this research project, we have created CNESSI, which contains 'structural' and 'semantic' information in the form of 'Knowledge-Share-Vectors (KSV)' embedded in each node (research document and each section of research document) of the Citation Network. The section-wise text organization adds 'structural' information and the quantified KSVs for each section and reseach document add the 'semantic' information to the citation network.

Detailed description of how this dataset was created, how this dataset will help for further research and possible applications that can be developed with this dataset have been explained in detail in the thesis (*CNESSI-Thesis*) put up in the repository.

### CNESSI Dataset Description.
CNESSI Dataset files are available in "CNESSI_Dataset.zip" file present in this repository. Please extract the zip file into a local folder.

This CNESSI dataset was created using the [ACL anthology reference corpus](https://aclanthology.info/papers/L08-1005/l08-1005).

###### Description of files in the CNESSI dataset:
1. doc_id_obj_dict.pickle: Serialized (Pickle) file containing the mapping from every research document_id to respective ResearchDocument python object. 

2. auth_id_obj_dict.pickle: Serialized (Pickle) file containing the mapping from every author_id to Author python object.

3. document_classes.py: The definitions of attributes of ResearchDocument and other python objects present in the dataset can be referred from this file. However, some of these attributes have not been populated and these could be populated in the future work.

4. venue_dict.pickle: Serialized (Pickle) file containing the mapping from every venue_id to venue_title.

###### The section id to section type mappings:
section_id_map = {1:"motivation", 2:"lit_survey", 3:"methodology", 4:"results", 5:"conclusion" }

###### The Knowledge Share Vector (ksv) mappings:
knowledge_topic_map = {1: 'NLP', 2:'InformationRetrieval', 3: 'ML', 4: 'DSA', 5: 'Systems'}.

KSV is a vector containing the knowledge share of the text in each of the above knowledge topics. Therefore, these terms are indexed from 0 for vector repesentation and hence the indices in the ksv are mapped as follows:

knowledge_topic_index_map = {0: 'NLP', 1:'InformationRetrieval', 2: 'ML', 3: 'DSA', 4: 'Systems'}.

Note that the 'Systems' knowledge topic has been referred as 'HPC' (High Performance Computing) in the thesis.

###### Dataset coverage:
The ACL dataset used to create this dataset is available in ACL website. Please refer the thesis for more details.
The document_id in CNESSI dataset corresponds to the document_id available in the ACL dataset. Hence the citation map in the ACL dataset can be used along with CNESSI dataset.

* Total number of research documents covered: 7995

* Total closed (internal) cited-to documents: 3356

### Data Exploration:
A sample code will be put up containing some sample code to explore different useful attributes available in the CNESSI dataset.

### Python modules used for creating the dataset:
lda-1.0.3, nltk-3.1, pattern-2.6, pbr-1.8.1, scikit-learn-0.16.1

### Affiliation:
**Bhuvan M S**, National Insitute of Technology Karnataka, Surathkal, Dept. Information Technology.

**Govind Sharma**, Indian Institue of Science, Dept. Computer Science and Automation, Topic Synthesis and Analysis Lab.*

**Prof. M Narasimha Murty**, Indian Institute of Science, Dept. Computer Science and Automation, Topic Synthesis and Analysis Lab.*

**Prof. Ananthanarayana. V. S**, National Institue of Technology Karnataka, Surathkal, Dept. Information Technology.*

### Contact:
Please feel free to contact by e-mailing to *msbhuvanbhuvi@gmail.com* for any queries. Please report any issues found in the dataset.

### Citation:
I will add a citation link soon, which can be used for citing any work inpsired from CNESSI dataset and research.
