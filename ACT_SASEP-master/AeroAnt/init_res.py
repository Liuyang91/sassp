__author__ = 'admin'

res_xml_file_path = "reslist_view.xml"
#res_xml_file_path = "res_list.xml"
from ResPool import client
client.reset_res_pool()
client.add_res_from_file(res_xml_file_path)