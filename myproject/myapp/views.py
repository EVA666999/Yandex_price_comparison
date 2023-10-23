from django.shortcuts import render
import requests
from decouple import config


def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        region_id = '2'
        token = config('TOKEN')

        min_price = float('inf')
        min_price_model = None

        page = 1
        total_results = []

        query_lower = query.lower()

        while True:
            url = f'https://api.partner.market.yandex.ru/v2/models?query={query}&regionId={region_id}&page={page}'

            if page > 50:
                break

            headers = {
                'Authorization': f'Bearer {token}',
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                results = data.get('models', [])
                if not results:
                    break
                total_results += results
            else:
                print(f'Ошибка при запросе: {response.status_code}')
                print(response.text)
                break

            page += 1

        filtered_results = [model for model in total_results if query_lower in model.get('name').lower()]
        print(f'Общее количество результатов для "{query}": {len(filtered_results)}')

        if filtered_results:
            for model in filtered_results:
                if 'prices' in model and 'min' in model['prices']:
                    price = model['prices']['min']
                    if price > 0 and price < min_price:
                        min_price = price
                        min_price_model = model

        return render(request, 'results.html', {'query': query, 'results': min_price_model})
    else:
        return render(request, 'index.html')
