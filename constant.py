# color the name of similar methods
COLORS = {'transformer':'RoyalBlue', 
          'CNN':'BrickRed',
         'MLP':'OliveGreen',
         'RNN':'SkyBlue',
         'statespace':'Orchid'}

METHODS_COLORS = {'DLinear':COLORS['MLP'],
                 'TSMixer':COLORS['MLP'],
                 'TimeMixer':COLORS['MLP'],
                 'Koopa':COLORS['MLP'],
                 'N-BEATS':COLORS['MLP'],
                 'Autoformer':COLORS['transformer'],
                 'Informer':COLORS['transformer'],
                 'PatchTST':COLORS['transformer'],
                 'Crossformer':COLORS['transformer'],
                 'Reformer':COLORS['transformer'],
                 'TFT':COLORS['transformer'],
                 'FEDformer':COLORS['transformer'],
                 'Pyraformer':COLORS['transformer'],
                 'Mamba':COLORS['statespace'],
                 'MICN':COLORS['CNN'],
                 'TimesNet':COLORS['CNN'],
                 'SegRNN':COLORS['RNN'],
                 'ETSformer':COLORS['transformer'],
                 'iTransformer':COLORS['transformer'],
                 'LightTS':COLORS['MLP']
                 }