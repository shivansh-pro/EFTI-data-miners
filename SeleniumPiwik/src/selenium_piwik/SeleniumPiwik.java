package selenium_piwik;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SeleniumPiwik {

	public static void main(String[] args)	throws InterruptedException{
		System.setProperty("webdriver.chrome.driver", "C:/Users/ssingh8008/Downloads/Selenium/chromedriver_win32/chromedriver.exe");
		/* To remove message "You are using an unsupported command-line flag: --ignore-certificate-errors. Stability and security will suffer." Add an argument 'test-type'*/
	    DesiredCapabilities capabilities = DesiredCapabilities.chrome();
	    ChromeOptions options = new ChromeOptions();
	    options.addArguments("test-type");
	    capabilities.setCapability("chrome.binary","C:/Users/ssingh8008/Downloads/Selenium/chromedriver_win32/chromedriver.exe");
	    capabilities.setCapability(ChromeOptions.CAPABILITY, options);

		WebDriver driver = new ChromeDriver(capabilities);

		driver.get("http://survey.modul.ac.at/piwikAnalytics/");
		WebDriverWait wait = new WebDriverWait(driver, 40);
		WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.id("login_form_submit")));
		element = driver.findElement(By.id("login_form_login"));
		Thread.sleep(1000);
		element.sendKeys("singh");
		element = driver.findElement(By.id("login_form_password"));
		Thread.sleep(1000);
		element.sendKeys("modul2015");
		element.submit();
		
		/*element = wait.until(ExpectedConditions.elementToBeClickable(By.id("Live_indexVisitorLog")));					//Trying to imitate mouse
		element = driver.findElement(By.id("Live_indexVisitorLog"));
		JavascriptExecutor executor = (JavascriptExecutor)driver;
		executor.executeScript("arguments[0].click();", element);
		
		element = wait.until(ExpectedConditions.elementToBeClickable(By.id("Live_indexVisitorLog")));*/
		
		/*driver.getCurrentUrl();
		driver.manage().timeouts().pageLoadTimeout(5, TimeUnit.SECONDS);*/
		
		/*WebElement myDynamicElement = (new WebDriverWait(driver, 10))
				  .until(ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='dataTable_5']/div[1]/div[1]")));*/
		
		wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.elementToBeClickable(By.className("UserCountryMap_container")));
		Actions actions = new Actions(driver);
		WebElement menuHoverLink = driver.findElement(By.xpath("//*[@id='VisitsSummary']/a"));
		actions.moveToElement(menuHoverLink);

		WebElement subLink = driver.findElement(By.id("Live_indexVisitorLog"));
		actions.moveToElement(subLink);
		actions.click();
		actions.perform();
		
		wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.className("dataTableFooterIcons")));
		String url = driver.getCurrentUrl();
		url=url+"&filter_limit=2000";
		driver.get(url);
		actions = new Actions(driver);
		wait = new WebDriverWait(driver, 10);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.className("dataTableFooterIcons")));
		
		element = wait.until(ExpectedConditions.elementToBeClickable(By.id("Live_indexVisitorLog")));
		element = driver.findElement(By.id("Live_indexVisitorLog"));
		JavascriptExecutor executor = (JavascriptExecutor)driver;
		executor.executeScript("arguments[0].click();", element);
		
		element = wait.until(ExpectedConditions.elementToBeClickable(By.id("Live_indexVisitorLog")));
		
		WebElement exportLink = driver.findElement(By.cssSelector("a[class='tableIcon'][var='export']"));
		actions.moveToElement(exportLink);
		actions.click();
		actions.perform();
				
		subLink = driver.findElement(By.cssSelector("a[format='TSV']"));
		actions.moveToElement(subLink);
		actions.click();
		actions.perform();
		
		Thread.sleep(5000);
		driver.quit();
	}
	
}
