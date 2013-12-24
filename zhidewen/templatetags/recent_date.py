# -*- coding: utf-8 -*-

from django import template
from django.utils import timezone
import datetime

register = template.Library()


@register.filter(name='recent_date')
def recent_date(date, now=None):
    """
    用和当前的时间差来格式化时间
        如 ‘1分钟前', '5天前', '12月12日'
    """
    if not now:
        now = timezone.now()
    timedelta = now - date
    if timedelta.days < 1:
        if timedelta.seconds <= 5:
            return u'刚刚'
        if timedelta.seconds < 60:
            return u'%s秒前' % timedelta.seconds
        if timedelta.seconds < 3600:
            return u'%s分钟前' % (timedelta.seconds/60)
        return u'%s小时前' % (timedelta.seconds/3600)
    if timedelta.days < 7:
        return u'%s天前' % timedelta.days
    # strptime 不支持 unicode，故此处用 %
    if date.year == now.year:
        return u'%s月%s日' % (date.month, date.day)
    return u'%s年%s月%s日' % (date.year, date.month, date.day)

