import sys

def main():
    print("============================================")
    print("      💰 AI EMPIRE ROI CALCULATOR 💰      ")
    print("============================================")
    print("Calculate your potential savings and revenue increase with AI.")
    print()

    try:
        # Input: Time Savings
        hours_saved_per_week = float(input("Estimated hours saved per week using AI (e.g., 10): "))
        hourly_rate = float(input("Your hourly value/rate (e.g., 50): "))

        # Input: Revenue Increase
        current_monthly_revenue = float(input("Current monthly revenue (e.g., 5000): "))
        expected_growth_percent = float(input("Expected growth percentage (e.g., 20 for 20%): "))

        # Calculations
        weekly_savings = hours_saved_per_week * hourly_rate
        monthly_savings = weekly_savings * 4
        annual_savings = monthly_savings * 12

        monthly_revenue_increase = current_monthly_revenue * (expected_growth_percent / 100)
        annual_revenue_increase = monthly_revenue_increase * 12

        total_monthly_benefit = monthly_savings + monthly_revenue_increase
        total_annual_benefit = annual_savings + annual_revenue_increase

        investment_cost = 147.00 # Price of AI Empire

        roi_percent = ((total_annual_benefit - investment_cost) / investment_cost) * 100

        print("\n============================================")
        print("           📊 YOUR RESULTS 📊           ")
        print("============================================")
        print(f"⏱️  Weekly Time Value Saved:   ${weekly_savings:,.2f}")
        print(f"💵 Monthly Value Created:     ${total_monthly_benefit:,.2f}")
        print(f"💰 Annual Value Created:      ${total_annual_benefit:,.2f}")
        print("--------------------------------------------")
        print(f"🚀 ROI on $147 Investment:    {roi_percent:,.0f}%")
        print("============================================")

        if roi_percent > 1000:
            print("\n🔥 Incredible! You are set for massive scaling.")
        elif roi_percent > 100:
            print("\n✅ Great! This is a solid investment for your business.")

    except ValueError:
        print("\n❌ Error: Please enter valid numbers.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nCalculator exited.")
        sys.exit(0)

if __name__ == "__main__":
    main()
