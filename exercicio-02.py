#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Tania Beatriz - exercicio 02

#construa um gráfico de barras vertical com os dados da distribuição da população feminina

import matplotlib.pyplot as plt

idade = ['0 a 4 anos','5 a 9 anos','10 a 14 anos','15 a 19 anos','20 a 24 anos',               '25 a 29 anos','30 a 34 anos','35 a 39 anos','40 a 44 anos','45 a 49 anos',                   '50 a 54 anos','55 a 59 anos','60 a 64 anos','65 a 69 anos','70 a 74 anos',                       '75 a 79 anos','80 a 84 anos','85 a 89 anos','90 a 94 anos','95 a 99 anos',                           '100 anos ou mais']

mas = [7016987,7624144,8725413,8558868,8630229,8460995,7717658,             6766664,6320568,5692014,4834995,3902344,3041035,2224065,                 1667372,1090517,668623,310759,114964,31529,7247]

fem = [6779171.0, 7345231.0, 8441348.0, 8432004.0, 8614963.0, 8643419.0, 8026854.0,            7121915.0, 6688796.0, 6141338.0, 5305407.0, 4373877.0, 3468085.0, 2616745.0,                2074264.0, 1472930.0, 998349.0, 508724.0, 211594.0, 66806.0, 16989.0]


plt.figure( figsize=(10, 8) )

x_pos = [ x for x in range(len(idade))]
plt.bar(idade,fem, color = 'red')
plt.title('Distribuição da população feminina por faixa etária - Brasil (2010)')

plt.xticks(x_pos, idade, rotation=45)
plt.show()

# In[ ]:




