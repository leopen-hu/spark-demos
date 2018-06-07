#  macD 麦氏久期
#  modD 修正久期

# parValue 票面价值
# residualMaturity 剩余期数 [次]
# couponRate 票面利率
# marketPrice 市场价格
# interestPaymentFrequency 付息频率（非标准英文） [次/年]

# 现金流 cashFlow

def calculate_cash_flow(parValue, couponRate, residualMaturity, ipf):
  return [parValue * couponRate / ipf if x < residualMaturity -1 else parValue * (1 + couponRate / ipf) for x in range(residualMaturity)]

# Yield To Maturity （ytm） 到期收益率
"""
每期【现金流】按【到期收益率】【贴现到当前的价格之和】等于当前的【市场价格】\
每期利息 = (票面价值 * 票面利率 * 付息频率)
市场价格 = 每期利息 / (1 + 到期收益率) + 每期利息 / (1 + 到期收益率) ** 2 + ... + 每期利息 / (1+到期收益率) ** (n-1) + (每期利息+票面价值) / (1+到期收益率) ** n
"""


def calculate_duration(cashFlow, ytm, ipv):
  cashFlowSum = sum(cashFlow)
  cashFlowDiscountSum = sum(value / (1 + ytm) ** ((index + 1) / ipv) * ((index + 1) / ipv) for (index, value) in enumerate(cashFlow))
  macD = cashFlowDiscountSum / cashFlowSum
  modD = macD / (1 + ytm)
  print(u'麦氏久期：', macD, u'修正久期：', modD)