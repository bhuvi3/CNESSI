import os
import pickle

# Run from directory containing CNESSI_Dataset or add the path containing 'document_classes.py' to the PYTHONPATH to make the module accessible to python.
cnessi_dataset_dir = "." 

doc_id_to_research_doc_dict = pickle.load(open(os.path.join(cnessi_dataset_dir, "doc_id_obj_dict.pickle")))

author_id_to_author_obj_dict = pickle.load(open(os.path.join(cnessi_dataset_dir, "auth_id_obj_dict.pickle")))

venue_id_to_venue_name_dict = pickle.load(open(os.path.join(cnessi_dataset_dir, "venue_dict.pickle")))

section_id_to_section_type_dict = {1: 'Motivation', 2: 'Background', 3: 'LiteratureReview', 4: 'Methodology', 5: 'ResultAndAnalysis', 6: 'ConclusionAndFutureWork'}
ksv_index_to_topic_name_dict = {0: 'NLP', 1:'InformationRetrieval', 2: 'ML', 3: 'DSA', 4: 'Systems'}

# Explore a research_document and get the author names.
print "\n# Get the title and author names of a research document.\n"
doc_ids = doc_id_to_research_doc_dict.keys()
doc_id = 'P03-1014' # These doc_id are the ones used in the ACL Anthology corpus.
research_document = doc_id_to_research_doc_dict[doc_id]
print "Research document title - %s (%s)" % (research_document.title, research_document.id)
for author in research_document.authors:
	print "Author: %s, %s" % (author.lname, author.fname)

# Get the KSV of a research_document and the KSV for each section of the research_document.
print "\n# Get the KSV of a research_document and the KSV for each section of the research_document.\n"
print "KSV of the document '%s' (%s): %s" % (research_document.title, research_document.id, research_document.ksv)
for section_id, section in research_document.sections.items():
	if section is None:
		print "The section type %s was not significantly identified in %s." % (section_id_to_section_type_dict[section_id], research_document.id)
	else:
		print ("Section type: %s\tSection KSV: %s"
			   % (section_id_to_section_type_dict[section_id], section.ksv))


# Get documents having closed citations (citattion where cited documents are also present in this dataset).
def get_closed_cited_doc_ids(doc_id_obj_dict):
	"""
	Get the doc_ids which have a closed citation in the dataset.

	"""
	closed_cited_doc_ids = []
	for doc_id, research_doc in doc_id_obj_dict.items():
		sections = [v for k, v in research_doc.sections.items() if v is not None]
		for section in sections:
			for citation in section.citations:
				if not citation.is_external:
					closed_cited_doc_ids.append(doc_id)

	return list(set(closed_cited_doc_ids))


closed_cited_doc_ids = get_closed_cited_doc_ids(doc_id_to_research_doc_dict)

# Find and print the KSV of the current research_document to the KSV of the a cited research_document. These KSVs can be compared as needed by the application.
print "\n# Find and print the KSV of the current research_document to the KSV of the a cited research_document. These KSVs can be compared as needed by the application.\n"
cited_doc_id = None
for section_id, section in research_document.sections.items():
	if section is not None:
		if len(section.citations) > 0:
			citation = section.citations[0]
			cited_doc_id = citation.cited_doc_id
			break

cited_to_research_document = doc_id_to_research_doc_dict[cited_doc_id]
print "The research document - %s (%s) has cited the research document - %s (%s)" % (research_document.title, research_document.id, cited_to_research_document.title, cited_to_research_document.id)

print "KSV comparison:\ncurrent research_document (%s) ksv: %s\ncited_to research_document (%s) ksv: %s" % (research_document.id, research_document.ksv, cited_to_research_document.id, cited_to_research_document.ksv)
