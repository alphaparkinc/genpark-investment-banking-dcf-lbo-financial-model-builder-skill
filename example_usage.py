from client import InvestmentBankingDcfLboFinancialModelBuilderClient

def main():
    client = InvestmentBankingDcfLboFinancialModelBuilderClient()
    res = client.build_institutional_financial_model('TECH_ENTERPRISE_TARGET', 'DISCOUNTED_CASH_FLOW_DCF', 10)
    print('Financial Model: ' + res['financial_model_id'] + ' (' + res['model_architecture'] + ')')
    print('IRR: ' + str(res['projected_irr_internal_rate_of_return_pct']) + '% | MOIC: ' + str(res['money_on_invested_capital_moic']) + 'x')
    print('10-K Tables Audited: ' + str(res['sec_10k_filing_tables_audited_count']) + ' | Memo Drafted: ' + str(res['investment_committee_memo_drafted']))

if __name__ == '__main__':
    main()
