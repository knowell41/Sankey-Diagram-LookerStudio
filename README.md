# SankeyDiagram4LookerStudio
Sankey Diagram Integration with Looker Studio Community Viz for [Material Flow Analysis](https://en.wikipedia.org/wiki/Material_flow_analysis).


## Bundling the Code

Looker Studio only allows one Javascript file. The uploaded code should be a single file that includes all the library and your own code.  

~~~
cd ./path/to/library
cat dscc.minjs d3.v4.minjs plotly-2.16.1.min.js template.js > index.js
~~~
The code snippet will create <i>index.js</i>. You can start working with your custom viz with it.

## Testing your viz
The following files needed to be uploaded to your Google Cloud Storage Bucket with each file available to public.
- <i>index.js</i>
- <i>index.json</i>
- <i>index.css</i>
- <i>manifest.json</i>

## Google Cloud Storage Automation with Python

1. Create Google Cloud Project
2. Go to APIs and Services >> Credentials.  
3. +Create credentials >> Service Account
4. Grant the service account access to Storage.
5. Creat a JSON key under the service account with access to storage.
6. Save the JSON key to /etc/yourJSONkey.json
7. Create *.env file for GCP bucket creds and save to /etc/yourENV.env
~~~
GOOGLE_APPLICATION_CREDENTIALS=/etc/yourJSONkey.json
BUCKET=your-bucket-name
DEV=your/dev/folder
PROD=your/prod/folder
TEST=your/test/folder/
PROJECTNAME=yourProjectName
~~~
8. Run build.py to automate the file upload to your dev/ua/prod bucket.  
~~~
$> Python build.py <target environment>
~~~
9. Test your viz!




## References

### Library
- Plotly: https://cdn.plot.ly/plotly-2.16.1.min.js <br>
- D3:<tr> https://d3js.org/d3.v4.min.js <br>
- DSCC: https://raw.githubusercontent.com/googledatastudio/tooling/master/packages/ds-component/_bundles/dscc.min.js <br>

### Resources
- Looker Studio: https://developers.google.com/looker-studio/visualization <br>
- Plotly Sankey JS Reference: https://plotly.com/javascript/reference/sankey/#sankey <br>
- Plotly Layout JS Reference: https://plotly.com/javascript/reference/layout/ <br>
- Google Cloud Storage: https://cloud.google.com/storage <br>


## Sample Dataset 1
[sample_data1.csv]( https://github.com/knowell41/SankeyDiagram4LookerStudio/blob/main/dataset/sample_data1.csv "sample_data1.csv")

| source | target | value |
| ------ | ------ | ----- |
| A | G | 1 |
| B | G | 10 |
| C | H | 1 |
| D | H | 10 |
| E | H | 1 |
| F | I | 10|

## Sankey Diagram with Looker Studio (dataset 1)
![dataset 1](https://github.com/knowell41/SankeyDiagram4LookerStudio/blob/main/image/sample1.png)

## Sample Dataset 2
[sample_data2.csv](https://github.com/knowell41/SankeyDiagram4LookerStudio/blob/main/dataset/sample_data2.csv "sample_data2.csv")

|X|Y|count|
|--|--|----|
|aa|aa|4|
|bb|ff|2|
|bb|gg|5|
|bb|ii|9|
|bb|jj|1|

## Sankey Diagram with Looker Studio (dataset 2)
![dataset 2](https://github.com/knowell41/SankeyDiagram4LookerStudio/blob/main/image/sample2.png)

## Live Demo Report
[Demo: Sankey](https://datastudio.google.com/reporting/aff1949a-e009-4ab9-adfc-21b37fc36382)


