# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
import re

from Job_51Spider.items import Job51Item


class Job51Spider(scrapy.Spider):
    name = 'Job51'
    allowed_domains = ['51job.com']
    industry_num = ['java']
    # industry_num = ['Java', 'C++', 'PHP', 'C', 'C#', '.NET', 'Hadoop', 'Python', 'Delphi', 'VB', 'Perl',
    #                 'Ruby', 'Node.js', 'Golang', 'Erlang', 'HTML5', 'Android', 'iOS', 'WP', 'Flash',
    #                 'JavaScript', 'U3D', 'COCOS2DX', '搜索算法', '自然语言处理', '推荐算法', '算法工程师',
    #                 '语音/视频/图形开发', '数据采集', '数据挖掘', '移动web前端', '测试工程师', '自动化测试',
    #                 '功能测试', '性能测试', '测试开发', '移动端测试', '游戏测试', '硬件测试', '软件测试',
    #                 '运维工程师', '运维开发工程师', '网络工程师', '系统工程师', 'IT技术支持', '系统管理员',
    #                 '网络安全', '系统安全', 'DBA', 'ETL工程师', '数据仓库', '数据开发', '数据挖掘',
    #                 '数据分析师', '数据架构师', '算法研究员', '实施工程师', '需求分析工程师', '技术经理',
    #                 '技术总监', '测试经理', '架构师', 'CTO', '运维总监', '人工智能', '机器学习', '深度学习',
    #                 '图像算法', '图像处理', '语音识别', '图像识别', '算法研究员', '售前工程师', '售后工程师']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,1.html'.format(x) for x in industry_num]
    # ''

    def parse(self, response):
        # '//*[@id="resultList"]/div[4]/p/span/a'
        # cout = 0
        le = LinkExtractor(restrict_xpaths='//*[@id="resultList"]/div[@class="el"]/p/span/a')
        # print(le)
        # le = LinkExtractor(restrict_css='ul>li div.info-primary>h3>a')
        for link in le.extract_links(response):
            # cout += 1
            # print(link.url, cout)
            yield scrapy.Request(link.url, callback=self.parse_book)
        le = LinkExtractor(restrict_xpaths='//*[@id="resultList"]/div[@class="dw_page"]/div/div/div/ul/li[last()]/a')
        # le = LinkExtractor(restrict_css='div.dw_wp div[]')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            # print(next_url)
            # yield scrapy.Request(next_url, callback=self.parse)

    def parse_book(self, response):
        item = Job51Item()
        try:
            item['position'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/h1/@title'
            ).extract_first()
        except:
            item['position'] = 'NULL'
        try:
            item['positionType'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/h1/@title'
            ).extract_first()
        except:
            item['positionType'] = 'NULL'
        try:
            item['salary'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/strong/text()'
            ).extract_first().split()[0]
        except:
            item['salary'] = 'NULL'
        try:
            item['city'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
            ).extract()[0].strip()
        except:
            item['city'] = 'NULL'
        try:
            item['firm'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="cname"]/a[@class="catn"]/@title'
            ).extract_first()
        except:
            item['firm'] = 'NULL'
        try:
            item['business'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_sidebar"]/div[@class="tBorderTop_box"]/div[@class="com_tag"]/p[3]/@title'
                ).extract_first()
        except:
            item['business'] = 'NULL'
        try:
            item['firmSize'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_sidebar"]/div[@class="tBorderTop_box"]/div[@class="com_tag"]/p[2]/@title'
                ).extract_first()
        except:
            item['firmSize'] = 'NULL'
        try:
            item['welfare'] = '|'.join(
                response.xpath(
                    '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/div[@class="jtag"]/div[@class="t1"]/span/text()'
                ).extract()
            )
        except:
            item['welfare'] = 'NULL'
        try:
            item['firmType'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_sidebar"]/div[@class="tBorderTop_box"]/div[@class="com_tag"]/p[1]/@title'
                ).extract_first()
        except:
            item['firmType'] = 'NULL'
        try:
            item['education'] = response.xpath(
                    '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
                ).extract()[2].strip()
        except:
            item['education'] = 'NULL'
        try:
            item['experience'] = response.xpath(
                    '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
                ).extract()[1].strip()
        except:
            item['experience'] = 'NULL'
        try:
            # item['positionDetail'] = response.xpath(
            position_detail = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_main"]/div[@class="tBorderTop_box"]/div[@class="bmsg job_msg inbox"]/p/text()'
            ).extract()
            position_detail_tmp = []
            for value in position_detail:
                position_detail_tmp.append(re.sub(r'[{}]+'.format(',\n :：；【】''，\xa0'), '', value))
            item['positionDetail'] = '|'.join(position_detail_tmp)
        except:
            item['positionDetail'] = 'NULL'
        try:
            item['time'] = response.xpath(
                    '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
                ).extract()[4].strip()
        except:
            item['time'] = 'NULL'
        try:
            item['numHire'] = response.xpath(
                '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
            ).extract()[3].strip()
        except:
            item['time'] = 'NULL'

        item['web'] = response.request.url
        #
        # yield item
        ######################################################################################
        # item['position'] = response.xpath(
        #     # '/html/body/div[3]/div[2]/div[2]/div/div[1]/h1'
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/h1/@title'
        # ).extract_first()
        # item['positionType'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/h1/@title'
        # ).extract_first()
        # item['salary'] = response.xpath(
        #     # ''
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/strong/text()'
        # ).extract_first().split()[0]
        # item['city'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
        # ).extract()[0].strip()
        # item['firm'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="cname"]/a[@class="catn"]/@title'
        # ).extract_first()
        # item['business'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_sidebar"]/div[@class="tBorderTop_box"]/div[@class="com_tag"]/p[3]/@title'
        #     ).extract_first()
        # item['firmSize'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_sidebar"]/div[@class="tBorderTop_box"]/div[@class="com_tag"]/p[2]/@title'
        #     ).extract_first()
        # item['welfare'] = '|'.join(
        #     response.xpath(
        #         '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/div[@class="jtag"]/div[@class="t1"]/span/text()'
        #     ).extract()
        # )
        # item['firmType'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_sidebar"]/div[@class="tBorderTop_box"]/div[@class="com_tag"]/p[1]/@title'
        #     ).extract_first()
        # item['education'] = response.xpath(
        #         '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
        #     ).extract()[2].strip()
        # item['experience'] = response.xpath(
        #         '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
        #     ).extract()[1].strip()
        # position_detail = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_main"]/div[@class="tBorderTop_box"]/div[@class="bmsg job_msg inbox"]/p/text()'
        # ).extract()
        # position_detail_tmp = []
        # for value in position_detail:
        #     position_detail_tmp.append(re.sub(r'[{}]+'.format(',\n :：；【】''，\xa0'), '', value))
        # item['positionDetail'] = '|'.join(position_detail_tmp)
        # item['time'] = response.xpath(
        #         '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
        #     ).extract()[4].strip()
        # item['numHire'] = response.xpath(
        #     '/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tHeader tHjob"]/div/div[@class="cn"]/p[@class="msg ltype"]/text()'
        # ).extract()[3].strip()
        #
        # item['web'] = response.request.url

        yield item
        # print(item)