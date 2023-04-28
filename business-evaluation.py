def dcf_analysis(net_profit, growth_rate, discount_rate, num_years, growth_rate_after_5_years):
    cash_flows = []

    # Calculate projected cash flows
    for year in range(1, num_years + 1):
        if year <= 5:
            cash_flow = net_profit * (1 + growth_rate) ** year
        else:
            cash_flow = cash_flows[-1] * (1 + growth_rate_after_5_years)
        cash_flows.append(cash_flow)

    # Calculate present value of cash flows
    pv_cash_flows = [cash_flow / (1 + discount_rate) ** year for year, cash_flow in enumerate(cash_flows, start=1)]

    # Calculate total present value of cash flows
    total_pv = sum(pv_cash_flows)

    return total_pv

# Inputs
net_profit = 75000
growth_rate = 0.30
discount_rate = 0.12
num_years = 10
growth_rate_after_5_years = 0.05

# Perform DCF analysis
business_value = dcf_analysis(net_profit, growth_rate, discount_rate, num_years, growth_rate_after_5_years)
print(f"Estimated business value: ${business_value:.2f}")

