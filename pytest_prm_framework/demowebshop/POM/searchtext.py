from demowebshop.POM.homepage import HomePage

class SearchText(HomePage):
    search_field=("id","small-searchterms")
    search_btn=("xpath","//input[@value='Search']")


    def search_the_Item(self,item) :
       self.send_text_to_element(self.search_field,item)
       self.click_on_an_element(self.search_btn)