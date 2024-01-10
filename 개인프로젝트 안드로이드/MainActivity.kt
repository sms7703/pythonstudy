import android.content.Context
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val interestRateEditText: EditText = findViewById(R.id.editTextInterestRate)
        val dividendEditText: EditText = findViewById(R.id.editTextDividend)
        val calculateButton: Button = findViewById(R.id.buttonCalculate)
        val resultTextView: TextView = findViewById(R.id.textViewResult)

        calculateButton.setOnClickListener {
            val interestRate = interestRateEditText.text.toString().toDoubleOrNull() ?: 0.0
            val dividend = dividendEditText.text.toString().toDoubleOrNull() ?: 0.0

            val totalAmount = calculateTotalAmount(interestRate, dividend)
            saveDataToPreferences(interestRate, dividend)

            resultTextView.text = "Total Amount: $totalAmount"
        }

        // Load and compare data when the app starts
        loadAndCompareData()
    }

    private fun calculateTotalAmount(interestRate: Double, dividend: Double): Double {
        // Implement your calculation logic here
        // For example, totalAmount = principal + (principal * interestRate) + dividend
        val principal = 1000.0
        return principal + (principal * interestRate) + dividend
    }

    private fun saveDataToPreferences(interestRate: Double, dividend: Double) {
        val sharedPreferences = getPreferences(Context.MODE_PRIVATE)
        val editor = sharedPreferences.edit()

        // Save data
        editor.putFloat("interest_rate", interestRate.toFloat())
        editor.putFloat("dividend", dividend.toFloat())

        editor.apply()
    }

    private fun loadAndCompareData() {
        val sharedPreferences = getPreferences(Context.MODE_PRIVATE)

        // Load saved data
        val savedInterestRate = sharedPreferences.getFloat("interest_rate", 0.0f)
        val savedDividend = sharedPreferences.getFloat("dividend", 0.0f)

        // Compare data or perform any other actions
        // For example, display a message based on the comparison
        val comparisonResult = compareData(savedInterestRate.toDouble(), savedDividend.toDouble())
        // Display the comparison result, you can customize this part based on your needs
        // resultTextView.text = "Comparison Result: $comparisonResult"
    }

    private fun compareData(savedInterestRate: Double, savedDividend: Double): String {
        // Implement your comparison logic here
        // For example, compare the current data with the saved data and return a message
        return if (savedInterestRate > 0 && savedDividend > 0) {
            "Data from previous calculation found. Compare or perform actions accordingly."
        } else {
            "No previous data found."
        }
    }
}
