from decimal import Decimal
from statistics import mean


def data_analysis(data):
    x_list = []
    y_list = []
    z_list = []

    for row in data:
        x_list.append(Decimal(f'{row.x}'))
        y_list.append(Decimal(f'{row.y}'))
        z_list.append(Decimal(f'{row.z}'))

    return {'x': {'minimum value': min(x_list),
                  'maximum value': max(x_list),
                  'number of values': len(x_list),
                  'sum of values': sum(x_list),
                  'median': mean(x_list)},
            'y': {'minimum value': min(y_list),
                  'maximum value': max(y_list),
                  'number of values': len(y_list),
                  'sum of values': sum(y_list),
                  'median': mean(y_list)},
            'z': {'minimum value': min(z_list),
                  'maximum value': max(z_list),
                  'number of values': len(z_list),
                  'sum of values': sum(z_list),
                  'median': mean(z_list)}
            }