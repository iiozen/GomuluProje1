/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/

#include "main.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "stdio.h"
#include "string.h"
#include "usart_islemler.h"
#include "I2C_LED.h"
#include "SPI_SICAKLIK.h"
#include "SPI_ADC.h"

char* UART1_RECIEVE[UART1_RECIEVE_ADET];
char* UART1_TRANSMIT[UART1_TRANSMIT_ADET];
char* sicaklik_adc[50];
int uzunlukverisi;

int tim2_sayici_led = 0;
int tim2_sayici_sicaklik = 0;
int tim2_sayici_adc = 0;
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart);
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim);
void Yapildi(void);
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  MX_I2C1_Init();
  MX_SPI2_Init();
  MX_TIM2_Init();
  MX_USART3_UART_Init();
  /* USER CODE BEGIN 2 */
  HAL_UART_Receive_IT(&huart1, UART1_RECIEVE, UART1_RECIEVE_ADET);


  HAL_TIM_Base_Start_IT(&htim2);
  /* BA�?LANGIÇ SICAKLIK SENSÖRÜNÜ BA�?LATIYORUM  */
  //SPI_SICAKLIK_BASLAT();
  /* BASLANGIÇ İÇİN TÜM LEDLERİ SÖNDÜRÜYORUM */
  I2C_LED_SONDUR(0xFFFF);

  /* BA�?LANGIÇ İÇİN MOTORUN HIZINI 0LIYORUM */
  I2C_MOTOR(0);

  /* BAŞLANGIÇ İLETİŞİM ÇIKIŞLARINI AYARLIYORUM */
	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOB, SPI_ADC_Pin, GPIO_PIN_SET);
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI_DIV2;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL8;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */
/* USART VERİ OKUMA İNTERRUPT */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	if(huart == &huart1)
	{

		int yapildi= Yap(UART1_RECIEVE);

		if (yapildi)
		{
			Yapildi();
		}
	}

}
/* TİMER İNTERRUPT */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{


	if(htim == &htim2)
	{
		tim2_sayici_led++;
		tim2_sayici_sicaklik++;
		tim2_sayici_adc++;

		if (I2C_LED_OTOMATIK_ARTIR)
		  {
			  if(tim2_sayici_led >= I2C_LED_DELAY_MS)
			  {
				  tim2_sayici_led = 0;
				  I2C_LED_SIRALI();
			  }
		  }

		if (SPI_SICAKLIK_OKU)
		  {
			  if(tim2_sayici_sicaklik >= SPI_SICAKLIK_OKUMA_DELAY)
			  {
				  tim2_sayici_sicaklik = 0;
				  SPI_SICAKLIK_ISLEMLER();
			  }
		  }
		if (SPI_ADC_OKU)
		  {
			  if(tim2_sayici_adc >= SPI_ADC_OKUMA_DELAY)
			  {
				  tim2_sayici_adc = 0;
				  SPI_ADC_ISLEMLER();
			  }
		  }




		/*
		  if(tim2_sayici_adc >= SPI_ADC_OKUMA_DELAY)
		  {
			  tim2_sayici_adc = 0;
		if (SPI_SICAKLIK_OKU)
		  {

				  tim2_sayici_sicaklik = 0;
				  tim2_sayici_adc = 0;
				  SPI_SICAKLIK_ISLEMLER();

			sprintf(sicaklik_adc,"SO%.4f",sicaklik);

		  }
		else
		{
			strcpy(sicaklik_adc,"SONone");

		}
		if (SPI_ADC_OKU)
		  {

				  SPI_ADC_ISLEMLER();

				  uzunlukverisi=sprintf(sicaklik_adc,"%s;AO%.3f\n",sicaklik_adc,adc_deger);

		  }
		else
		{
			uzunlukverisi=sprintf(sicaklik_adc,"%s;AO%s\n\r",sicaklik_adc,"None");
		}
		if (SPI_SICAKLIK_OKU | SPI_ADC_OKU)
		{
			HAL_UART_Transmit(&huart3, sicaklik_adc, uzunlukverisi, HAL_MAX_DELAY);
		}
		  }
		  */




	}

}


void Yapildi(void)
{
	HAL_UART_Transmit(&huart1, UART1_TRANSMIT_ONAY, UART1_TRANSMIT_ADET, HAL_MAX_DELAY);
	HAL_UART_Receive_IT(&huart1, UART1_RECIEVE, UART1_RECIEVE_ADET);
}

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
