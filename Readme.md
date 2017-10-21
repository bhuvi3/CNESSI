# CNESSI
Citation Network with Enhanced Structural and Semantic Information.

Detailed description of how this dataset was created, how this dataset will help for further research and possible applications that can be developed with this dataset have been explained in detail in the thesis (*CNESSI-Thesis*) put up in the repository.

### Dataset Description:
Dataset link will be added soon.

###### Description of files in the dataset:
1. doc_id_obj_dict.pickle: Serialized (Pickle) file containing the mapping from every research document_id to respective ResearchDocument python object. 

2. auth_id_obj_dict.pickle: Serialized (Pickle) file containing the mapping from every author_id to Author python object.

3. document_classes.py: The attributes of the classes are clearly defined in document_classes.py. It can be used a reference, but some of the attributes are not populated and these could be populated in the future work.

4. venue_dict.pickle: Serialized (Pickle) file containing the mapping from every venue_id to venue_title.

###### The section id to section type mappings:
{1:"motivation", 2:"lit_survey", 3:"methodology", 4:"results", 5:"conclusion" }

###### The Knowledge Share Vector (ksv) mappings:
KT = {1: 'NLP', 2:'InformationRetrieval', 3: 'ML', 4: 'DSA', 5: 'Systems'}.

In a ksv, these terms are changed to index 0 for vector repesentation and hence the index in the ksv are mapped as follows:

{0: 'NLP', 1:'InformationRetrieval', 2: 'ML', 3: 'DSA', 4: 'Systems'}

Note that the 'Systems' knowledge topic has been referred as 'HPC' (High Performance Computing) in the thesis.

###### Dataset coverage:
The dataset used is available in ACL website. Refer the thesis for more details.
The document_id corresponds to the document_id available in the ACL dataset. Hence the citation map in the ACL dataset can be used along with our dataset.

Total number of research documents covered: 7995
Total closed (internal) cited-to documents: 3356

### Data Exploration:
A sample code will be put up containing some simple code to explore different useful attributes available in the dataset.

### Python modules used for creating the dataset.
lda-1.0.3
nltk-3.1
pattern-2.6
pbr-1.8.1
scikit-learn-0.16.1

Please feel free to contact me on *msbhuvanbhuvi@gmail.com* for any queries. Please report any issues found in the dataset.

I will add a citation link soon, which can be used for citing any work based of this dataset and research.

Thank you  
Bhuvan
