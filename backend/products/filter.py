class ProductFilterBackend:
    def filter_queryset(self, request, queryset, view):
        filters = {}

        bool_params = {
            'product_discount': 'product_discount',
            'product_international': 'product_international'
        }

        for param, field in bool_params.items():
            value = request.query_params.get(param)
            if value is not None:
                filters[field] = value.lower() == 'true'

        product_type = request.query_params.get('product_type')
        if product_type:
            print(product_type)
            types = [item.strip() for item in product_type.split(',')]
            filters['product_type__in'] = types

        product_category = request.query_params.get('product_category')
        if product_category:
            categories = [item.strip() for item in product_category.split(',')]
            filters['category__name__in'] = categories

        return queryset.filter(**filters)
