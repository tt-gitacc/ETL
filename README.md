# ETL
The objective of this lab was to transform a raw dataset into a file that could be processed easily by LibSVM (a Support Vector Machine used for statistical machine learning and data classification purposes). 
The dataset in question contained income-related data that had been acquired by the US Census Bureau, and contained both categorical and ordinal data types.<br>
<br>
I began by scanning the original data set for mutually exclusive values associated with each attribute, then mapped them to new IDs. I then iterated through the input file a second time so I could
assign a unique identifier to each unique value: this resulted in the adult.libsvm file I attached.
