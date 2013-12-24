#-*- encoding: utf-8 -*-

from django.test import TestCase
from zhidewen.templatetags.recent_date import recent_date
import datetime


class TestRecentDate(TestCase):

    def assertDatetime(self, expect, date_str, date_now_str):
        p = lambda s: datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
        self.assertEqual(expect, recent_date(p(date_str), p(date_now_str)))

    def test_recent_date(self):

        self.assertDatetime(u'刚刚', '2013-01-01 00:00:00', '2013-01-01 00:00:00')
        self.assertDatetime(u'刚刚', '2013-01-01 00:00:00', '2013-01-01 00:00:05')
        self.assertDatetime(u'6秒前', '2013-01-01 00:00:00', '2013-01-01 00:00:06')
        self.assertDatetime(u'59秒前', '2013-01-01 00:00:00', '2013-01-01 00:00:59')
        self.assertDatetime(u'1分钟前', '2013-01-01 00:00:00', '2013-01-01 00:01:00')
        self.assertDatetime(u'59分钟前', '2013-01-01 00:00:00', '2013-01-01 00:59:59')
        self.assertDatetime(u'1小时前', '2013-01-01 00:00:00', '2013-01-01 01:00:00')
        self.assertDatetime(u'23小时前', '2013-01-01 00:00:00', '2013-01-01 23:59:59')
        self.assertDatetime(u'1天前', '2013-01-01 00:00:00', '2013-01-02 00:00:00')
        self.assertDatetime(u'6天前', '2013-01-01 00:00:00', '2013-01-07 23:59:59')
        self.assertDatetime(u'1月1日', '2013-01-01 00:00:00', '2013-01-08 00:00:00')
        self.assertDatetime(u'2012年12月31日', '2012-12-31 00:00:00', '2013-01-08 00:00:00')