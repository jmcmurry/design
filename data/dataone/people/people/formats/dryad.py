""" dryad.py

    Processing functions for processing Dryad metadata

    TODO: Handle the XML entities Jonnson and stuff. See Dryad.
"""

from people import find


def process(job, xmldoc, document):
    """
        Process XML document `xmldoc` with identifier `document` as if it
        is an EML document.
    """

    # Process each <creator>
    creators = xmldoc.findall(".//ns2:creator", { 'ns2': 'http://purl.org/dc/terms/'})

    records = []

    for creator in creators:
        if creator.text is None:
            continue

        record = {}
        name = creator.text.strip()

        name_parts = name.split(",")

        # Check if "Last, First" is plausible
        if len(name_parts) == 2:
            record['first_name'] = name_parts[1]
            record['last_name'] = name_parts[0]
            record['name'] = ' '.join(name_parts[1], name_parts[2])

        record['format'] = "Dryad"
        record['type'] = 'person'
        record['document'] = document

        records.append(record)

    return records
