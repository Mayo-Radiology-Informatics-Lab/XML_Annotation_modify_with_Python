# XML_Annotation_modify_with_Python
XML annotation format commonly used in Imagescope and modyfying the color of annotation for every image could be cumbersome. This script helps to change the color of annotation and could be useful to adapt for other task.

## Provide the folder paths:
xml_path= r'xml_folder' <br />
mask_output =r"xml_newoutput" <br />

 Provide the label you want to change color for; e.g 'NSG_area2s': <br />
if re.findall(r'Name=\"NSG_area2s\".*LineColor=\"(\d+)\"', line): <br />
## Provide the new color for label NSG_area2s; '255' is for red here:
line=re.sub(r'LineColor=\"(\d+)\"',r'LineColor="255"', line) <br />

List of color to choose: <br />
255 and 8388863 for red <br />
0 for black  <br />
65535 for yellow <br />
65280 for green <br />
4227327 for Brown <br />



The XML annotation format exmaple is as follows, where 'LineColor' is annotation color.
![XML](https://user-images.githubusercontent.com/65933407/221015131-12c7c22f-5bf8-4cdb-95d5-8a739022ca09.png)
