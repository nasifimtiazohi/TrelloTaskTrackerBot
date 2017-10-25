package selenium.tests;

import static org.junit.Assert.*;
import org.junit.runners.MethodSorters;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
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

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class BotTest
{
	private static WebDriver driver;
	private static String lastTime;
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

		
		//*[@id="msg_1508897624_000178"]/div[2]/div[1]/div/span[2]/a
		String path = "//div[@id='msgs_div']/div[1]/div[2]/ts-message[last()]//span[@class = 'message_body' and text() = 'sheikhnasifimtiaz is asked to complete example task 4']";
		WebElement slackbot  = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(path)));
		//WebElement time = driver.findElement(By.xpath("div[@id='msgs_div']/div[1]/div[2]/ts-message[last()-3]/div[2]/div[1]/div/span[2]/a"));
		List<WebElement> times = driver.findElements(By.xpath("//span[@class = 'time_star_and_extra_metadata']/a"));
		
		lastTime = times.get(times.size() -4).getText();
		System.out.println("Time: "+lastTime);
		
		//System.out.println("Time: "+times.get(times.size() -3).getText());
//		for(WebElement time: times) {
//			
//			System.out.println("Time ARRAY: "+time.getText());
//		}
		//*span[@class = 'time_star_and_extra_metadata']/a/text()
		assertNotNull(slackbot);
		
	}
	
	@Test
	public void testEmailSent() throws InterruptedException
	{
	
		driver = new ChromeDriver();
		driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin");

		String GMAIL_USERNAME = "bot510project@gmail.com";
		String GMAIL_PASSWORD = "simtiaz1234";

		//Enter the email id 		
		driver.findElement(By.id("identifierId")).sendKeys(GMAIL_USERNAME);
		//Click Next Button
		driver.findElement(By.id("identifierNext")).click();
		Thread.sleep(1000);
		
		driver.findElement(By.xpath("//input[@aria-label='Enter your password' and @name='password']")).sendKeys(GMAIL_PASSWORD); 
		Thread.sleep(1000);
		//Click Next Button
		driver.findElement(By.id("passwordNext")).click();
		Thread.sleep(3000);
	
		driver.findElement(By.xpath("//*[@id=':4n']/div/div[2]/span/a")).click();
		Thread.sleep(8000);
	   //td[@class = 'yX xY'] 
		List<WebElement> emails = driver.findElements(By.xpath("//tbody/tr"));
		
		//System.out.println("email: "+email.getText());
		String simtiaz  = emails.get(9).getText();
		String vgupta8  = emails.get(10).getText();
		String xfu7 = emails.get(11).getText();
		
		System.out.println("email 2: "+emails.get(9).getText());
		System.out.println("email 2: "+emails.get(10).getText());
		System.out.println("email 2: "+emails.get(11).getText());
		
		assertTrue(simtiaz.contains("simtiaz"));
		assertTrue(simtiaz.contains(lastTime.toLowerCase()));
		assertTrue(vgupta8.contains("vgupta8"));
		assertTrue(vgupta8.contains(lastTime.toLowerCase()));
		assertTrue(xfu7.contains("xfu7"));
		assertTrue( xfu7.contains(lastTime.toLowerCase()));
	}
	
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
