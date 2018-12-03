def all_re():
    re_dict = dict(
        city_All = '<p class="msg ltype" (.*?)>',
        city1 = 'title="(.*?)&nbsp;&nbsp;|',

    skill_type = '<h1 title="(.*?)">\
',
    company_name = '<a href=".*?" target="_blank" title="(.*?)" class="catn">\
',

    company_description = '<p class="at" title="(.*?)">\
',
    company_location = '<span class="label">上班地址：</span>(.*?)							</p>\
',
    job_required = '<div class="bmsg job_msg inbox">(.*?)<div class="mt10">',
    # edu_required = '<p class="msg ltype" title="(.*?)">\',
    experience_required = '&nbsp;&nbsp;(.*?)经验',
    company_welfare = '<span class="sp4">(.*?)</span>\
',

    salary = '<strong>(.*?)</strong>\
',)


    return re_dict
