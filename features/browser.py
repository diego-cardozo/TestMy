from selenium import webdriver


class Browser(object):

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    def go_to(self, url=''):
        """
        Go to url passed as parameter
        :param url: should be a valid url
        """
        self.driver.get(url)

    def get_current_url(self):
        """
        Get the current navigation url
        """
        return str(self.driver.current_url)

    def query_selector_css(context, selector):
        """
        Get web element by CSS selector
        """
        return context.driver.find_element_by_css_selector(selector)

    def query_selector_name(context, name):
        """
        Get web element by Text link
        """
        return context.driver.find_element_by_name(name)

    def close(self):
        """
        close web driver instance
        """
        self.driver.quit()

    def query_selector_xpath(context, xpath):
        return context.driver.find_element_by_xpath(xpath)

    def get_iframe(context, iframe_name):
        context.driver.switch_to.frame(context.driver.find_element_by_css_selector(iframe_name))

    def query_selector_id(context, idweb):
        return context.driver.find_element_by_id(idweb)



