from rest_framework.pagination import PageNumberPagination, _positive_int


class CustomPageNumberPagination(PageNumberPagination):
	# max_page_size = 1000
	page_size_query_param = "page_size"  # items per page

	def get_page_size(self, request):
		if self.page_size_query_param:
			try:
				page_size_query_value = request.query_params[self.page_size_query_param]
				if page_size_query_value == "max":
					if self.max_page_size:
						return self.max_page_size
					else:
						return 1_000000_000000
				return _positive_int(page_size_query_value, strict=True, cutoff=self.max_page_size)
			except (KeyError, ValueError):
				pass

		return self.page_size
