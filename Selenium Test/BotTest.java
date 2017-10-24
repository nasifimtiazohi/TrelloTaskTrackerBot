package selenium.tests;

import static org.junit.Assert.*;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.ChromeDriverManager;

public class BotTest
{
	private static WebDriver driver;
	
	@BeforeClass
	public static void setUp() throws Exception 
	{
		//driver = new HtmlUnitDriver();
		ChromeDriverManager.getInstance().setup();
	}


	@AfterClass
	public static void  tearDown() throws Exception
	{
		driver.close();
		driver.quit();
	}
	
	/**
	 * Use case 1: Send Nagging Reminder
	 * Test the following functionalities:
	 * Fetches cards that are due within 1 day deadline (I actually didn't compare the due dates. I just put the mock data in one list. it won't be difficult to check). 
	 * Detect the members assigned to that task.
	 * Sends a message to general channel that this user required to this task(card name) and also 
	 * Sends a Email to his/her email
	 * 
	 * */
	
	@Test
	public void sendNaggingReminder()
	{
		driver = new ChromeDriver();
		driver.get("https://" + System.getenv("SLACK_WEB_ADDRESS") + "/");
		// Wait until page loads and we can see a sign in button.
		WebDriverWait wait = new WebDriverWait(driver, 20);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn")));

		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		WebElement pw = driver.findElement(By.id("password"));

		// Enter our email and password
		// If running this from Eclipse, you should specify these variables in the run configurations.
		email.sendKeys(System.getenv("SLACK_EMAIL"));
		pw.sendKeys(System.getenv("SLACK_PASSWORD"));
		
		// Click
		WebElement signin = driver.findElement(By.id("signin_btn"));
		signin.click();
		// Wait until we go to general channel.
		wait.until(ExpectedConditions.titleContains("general"));
		// Input Command to the bot
		WebElement messageBot = driver.findElement(By.id("msg_input"));
		assertNotNull(messageBot);
			
		Actions actions = new Actions(driver);
		actions.moveToElement(messageBot);
		actions.click();
		
		//The designed command is "@firsttest usecase 1" here
		actions.sendKeys("@firsttest usecase 1");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();

		String path = "//div[@id='msgs_div']/div[1]/div[2]/ts-message[last()]//span[@class = 'message_body' and text() = 'sheikhnasifimtiaz is asked to complete example task 4']";
		WebElement slackbot  = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(path)));
	    
		assertNotNull(slackbot);
		
	
	}
	
//	@Test
//	public void testEmailSent()
//	{
//		
//		driver.get("https://" + System.getenv("SLACK_WEB_ADDRESS") + "/");
//
//		// Wait until page loads and we can see a sign in button.
//		WebDriverWait wait = new WebDriverWait(driver, 30);
//		
//		wait.until(ExpectedConditions.titleContains("general"));
//
//		// Input Command to the bot
//		WebElement messageBot = driver.findElement(By.id("msg_input"));
//		assertNotNull(messageBot);
//			
//		Actions actions = new Actions(driver);
//		actions.moveToElement(messageBot);
//		actions.click();
//		
//		//The designed command is "@firsttest usecase 1" here
//		actions.sendKeys("@firsttest usecase 1");
//		actions.sendKeys(Keys.RETURN);
//		actions.build().perform();
//
//		wait.withTimeout(5, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
// 
//		//It should find the response of the bot
//		WebElement msg = driver.findElement(
//				By.xpath("//span[@class='message_body' and text() = 'vinay638: 130 sheikhnasifimtiaz: 80 xiaotingfu1: 205 otto292: 235 guanxuyu: 290']"));
//	
//		
//		//Test if the email is sent
//		assertNotNull(msg);
//	}
//	/**
//	 * Use case 2: Calculate Rewards based on Team Members’ Performance
//	 * Test the following functionalities:
//	 * Fetch the performance score for each member
//	 * 
////	 * */
	
	@Test
	public void performanceEvaluation()
	{
		driver = new ChromeDriver();
		driver.get("https://" + System.getenv("SLACK_WEB_ADDRESS") + "/");
		// Wait until page loads and we can see a sign in button.
		
		//driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		WebDriverWait wait = new WebDriverWait(driver, 15);
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn")));

		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		WebElement pw = driver.findElement(By.id("password"));

		// Enter our email and password
		// If running this from Eclipse, you should specify these variables in the run configurations.
		email.sendKeys(System.getenv("SLACK_EMAIL"));
		pw.sendKeys(System.getenv("SLACK_PASSWORD"));
		
		// Click
		WebElement signin = driver.findElement(By.id("signin_btn"));
		signin.click();
		// Type something
		WebElement messageBot = driver.findElement(By.id("msg_input"));
		assertNotNull(messageBot);
			
		Actions actions = new Actions(driver);
		actions.moveToElement(messageBot);
		actions.click();
		actions.sendKeys("@firsttest usecase 2");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();
		
		String path = "//div[@id='msgs_div']/div[1]/div[2]/ts-message[last()]//span[@class = 'message_body' and text() = 'guanxuyu: 0']";
		WebElement slackbot  = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(path)));
	    
		assertNotNull(slackbot);
	}
//	
//	/**
//	 * Use case 3: Reminder Buddy
//	 * Send Direct message to the person
//	 * 
//	 * */
	@Test
	public void reminderBuddy()
	{
		driver = new ChromeDriver();
		driver.get("https://" + System.getenv("SLACK_WEB_ADDRESS") + "/");
		// Wait until page loads and we can see a sign in button.
		WebDriverWait wait = new WebDriverWait(driver, 5);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn")));

		// Find email and password fields.
		WebElement email = driver.findElement(By.id("email"));
		WebElement pw = driver.findElement(By.id("password"));

		// Enter our email and password
		// If running this from Eclipse, you should specify these variables in the run configurations.
		email.sendKeys(System.getenv("SLACK_EMAIL"));
		pw.sendKeys(System.getenv("SLACK_PASSWORD"));
		
		// Click
		WebElement signin = driver.findElement(By.id("signin_btn"));
		signin.click();
		// Switch to #selenium-bot channel and wait for it to load.
		driver.get("https://" + System.getenv("SLACK_WEB_ADDRESS")  + "/messages/firsttest/");
		wait.until(ExpectedConditions.titleContains("firsttest"));

		// Type something
		WebElement messageBot = driver.findElement(By.id("msg_input"));
		assertNotNull(messageBot);
			
		Actions actions = new Actions(driver);
		actions.moveToElement(messageBot);
		actions.click();
		actions.sendKeys("@firsttest usecase 3");
		actions.sendKeys(Keys.RETURN);
		actions.build().perform();

		//wait.withTimeout(5, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);
		String path = "//div[@id='msgs_div']/div[1]/div[2]/ts-message[last()]//span[@class = 'message_body' and text() = 'what is your progress, mate?']";
		//WebElement test = driver.findElement(By.xpath(path))
		WebElement test  = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(path)));
		
		//System.out.println(test.getText());
		assertNotNull(test);
		
	}
}
