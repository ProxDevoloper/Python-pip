#1
import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.usd_to_kzt = self.get_usd_to_kzt_ruble()
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        
        table = soup.find('table', class_='table-rates')

        if not table:
            raise ValueError("Не удалось найти таблицу с курсами валют.")

        
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) > 1 and 'USD' in columns[0].text:

                try:
                    rate = float(columns[1].text.strip().replace(",", "."))
                    print(f"Найден курс доллара: {rate} KZT/USD")
                    return rate
                except ValueError:
                    raise ValueError("Не удалось правильно распарсить курс доллара.")

        raise ValueError("Не удалось найти курс доллара на странице.")

    def convert_to_usd(self, amount):
        """Конвертирует количество тенге в доллары США."""
        return amount / self.usd_to_kzt

def main():
    try:
        converter = CurrencyConverter()  
        print(f"Текущий курс доллара: {converter.usd_to_kzt} KZT/USD")

        while True:
            try:
                amount = float(input("Введите сумму в тенге: ")) 
                result = converter.convert_to_usd(amount)  
                print(f"Эквивалент в долларах США: ${result:.2f}")
            except ValueError:
                print("Введите корректное число.")
            except KeyboardInterrupt:
                print("\nВыход из программы.")
                break
    except Exception as e:
        print(f"Ошибка при получении курса доллара: {e}")

if __name__ == "__main__":
    main()
#ЗАДАНИЕ 2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self):
        self.df = self.get_exchange_rates()  # Загружаем курсы в DataFrame
    
    def get_exchange_rates(self):
        """Парсит курс валют с сайта Halyk Bank и возвращает DataFrame."""
        url = "https://halykbank.kz/exchange-rates"
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='table-rates')
        
        if not table:
            raise ValueError("Не удалось найти таблицу с курсами валют.")
        
        rows = table.find_all('tr')
        
        data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) > 1:
                currency = columns[0].text.strip()
                rate = columns[1].text.strip().replace(",", ".")
                data.append([currency, rate])
        
       
        df = pd.DataFrame(data, columns=['Валюта', 'Курс'])
        return df

    def convert_to_usd(self, amount):
        """Конвертирует количество тенге в доллары США."""
        usd_rate = float(self.df[self.df['Валюта'] == 'USD']['Курс'].values[0])
        return amount / usd_rate

class CurrencyConverterApp:
    def __init__(self, root):
        self.converter = CurrencyConverter()  
        self.root = root
        self.root.title("Конвертер валют")
        
        
        self.label1 = tk.Label(root, text="Введите сумму в тенге:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.result_label = tk.Label(root, text="Результат конвертации: $0.00")
        self.result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.convert_button = tk.Button(root, text="Конвертировать", command=self.convert)
        self.convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    def convert(self):
        """Обрабатывает событие нажатия кнопки и конвертирует валюту."""
        try:
            amount = float(self.amount_entry.get())  
            result = self.converter.convert_to_usd(amount)  
            self.result_label.config(text=f"Результат конвертации: ${result:.2f}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def main():
    root = tk.Tk()  
    app = CurrencyConverterApp(root)  
    root.mainloop()  

if __name__ == "__main__":
    main()
