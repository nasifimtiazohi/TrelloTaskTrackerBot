@Test
public void postMessage()
{
	driver.get("https://510taskmanagerbot.slack.com/");

	// Wait until page loads and we can see a sign in button.
	WebDriverWait wait = new WebDriverWait(driver, 30);
	wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("signin_btn")));

	// Find email and password fields.
	WebElement email = driver.findElement(By.id("email"));
	WebElement pw = driver.findElement(By.id("password"));

	// Type in our test user login info.
	email.sendKeys("xfu7@ncsu.edu");
	pw.sendKeys("TTyy3344/");

	// Click
	WebElement signin = driver.findElement(By.id("signin_btn"));
	signin.click();

	// Wait until we go to general channel.
	wait.until(ExpectedConditions.titleContains("general"));

	// Switch to #bots channel and wait for it to load.
	driver.get("https://csc510-fall16.slack.com/messages/bots");
	wait.until(ExpectedConditions.titleContains("bots"));

	// Type something
	WebElement messageBot = driver.findElement(By.id("message-input"));
	messageBot.sendKeys("hello world, from Selenium");
	messageBot.sendKeys(Keys.RETURN);

	wait.withTimeout(3, TimeUnit.SECONDS).ignoring(StaleElementReferenceException.class);

	WebElement msg = driver.findElement(
			By.xpath("//span[@class='message_body' and text() = 'hello world, from Selenium']"));
	assertNotNull(msg);
}