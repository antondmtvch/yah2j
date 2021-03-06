from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class SimpleController(BasicController, IncludesElements, Renderable):

    root_element_name = 'GenericController'
    TEMPLATE = 'simple_controller_template.xml'

    def __init__(self, *,
                 name: str = 'Simple Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        IncludesElements.__init__(self)
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
