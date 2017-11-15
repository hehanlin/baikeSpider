# -*- coding: utf-8 -*-


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()   # 未爬取url集合
        self.old_urls = set()   # 已爬取url集合

    def new_urls_sizes(self):
        return len(self.new_urls)

    def old_urls_sizes(self):
        return len(self.old_urls)

    def has_new_url(self):
        """
        判断是否拥有未爬取的url
        :return: 
        """
        return self.new_urls_sizes() != 0

    def get_new_url(self):
        """
        获取一个未爬取的url
        :return:
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        将新的url添加进去
        :param url: 
        :return: 
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        多次添加
        :param urls: 
        :return: 
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)