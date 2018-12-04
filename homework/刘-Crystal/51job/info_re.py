def all_re():

    re_dict = dict(

        #
        city_All='<p class="msg ltype" (.*?)>',
        # 城市
        city1='title="(.*?)&nbsp;&nbsp;|',
        # 技能
        skill_type='<h1 title="(.*?)">\
',
        # 公司名字
        company_name='<a href=".*?" target="_blank" title="(.*?)" class="catn">\
',
        # 公司描述
        company_description='<p class="at" title="(.*?)">\
',
        # 公司位置
        company_location='<span class="label">上班地址：</span>(.*?)							</p>\
',
        # 工作需求
        job_required='<div class="bmsg job_msg inbox">(.*?)<div class="mt10">',
        # 经验需求
        experience_required='&nbsp;&nbsp;(.*?)经验',
        # 公司福利
        company_welfare='<span class="sp4">(.*?)</span>\
',
        # 薪资
        salary='<strong>(.*?)</strong>\
',)

    return re_dict
