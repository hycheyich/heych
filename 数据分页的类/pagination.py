# 分页class


class Pagination:
    def __init__(self, page, count_data, per_num=10, max_show=11):
        """
        :param page: 页码
        :param count_data: 数据总数量
        :param per_num: 页面中最多显示的数据行数
        :param max_show:页面中最多显示的页码数
        """
        try:
            page = int(page)
            if page <= 0:
                page = 1
        except Exception:
            page = 1

        self.page = page
        self.per_num = per_num
        self.count_data = count_data
        self.max_show = max_show
        self.sum_page_num_nu = 0
        self.sum_page_num = 0

    @property
    def start(self):
        if (self.page - 1) * self.per_num > self.count_data:
            self.page = self.sum_pagination()
        return (self.page - 1) * self.per_num

    @property
    def end(self):
        if self.page * self.per_num > self.count_data:
            self.page = self.sum_pagination()
        return self.page * self.per_num

    def sum_pagination(self):
        self.sum_page_num, self.more = divmod(self.count_data, self.per_num)  # 计算总页码数
        if self.more:  # 有余数时，页码数+1
            self.sum_page_num += 1
        return self.sum_page_num

    @property
    def page_html(self):
        """
        :return:页面显示的html代码
        """
        self.sum_page_num_nu = self.sum_pagination()

        half_show = self.max_show // 2

        if self.sum_page_num_nu < self.max_show:
            # 页码数量超过显示的最大页码数
            page_start = 1
            page_end = self.sum_page_num_nu
        else:
            if self.page - half_show < 0:
                page_start = 1
                page_end = self.max_show
            elif self.page + half_show > self.sum_page_num_nu:
                page_end = self.sum_page_num_nu
                page_start = self.sum_page_num_nu - self.max_show + 1
            else:
                page_start = self.page - half_show
                page_end = self.page + half_show
        page_html_lis = []
        if self.page == 1:
            page_html_lis.append(
                '<li class="disabled"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            page_html_lis.append(
                '<li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.page - 1))
        for i in range(page_start, page_end + 1):
            if i == self.page:
                page_html_lis.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
            else:
                page_html_lis.append('<li><a href="?page={}">{}</a></li>'.format(i, i))
        if self.page == self.sum_page_num_nu:
            page_html_lis.append(
                '<li class="disabled"><a aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            page_html_lis.append(
                '<li><a href="?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.page + 1))

        st = "".join(page_html_lis)
        return mark_safe(st)
