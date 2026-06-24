import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()


def main():
    print("Hello from langchain-ai-project!")
    information="""
Microsoft Corporation is an American multinational technology company headquartered in Redmond, Washington. The company became influential in the rise of personal computers through software like Windows and has since expanded into areas such as Internet services, cloud computing, artificial intelligence, video gaming, and more. A Big Tech company, Microsoft is the largest software company by revenue, one of the most valuable public companies, and one of the most valuable brands globally.

Founded in 1975 by Bill Gates and Paul Allen to market BASIC interpreters for the Altair 8800, Microsoft rose to dominate the PC operating system market with MS-DOS in the mid-1980s, followed by Windows. The company's 1986 initial public offering (IPO) and subsequent rise in its share price created three billionaires and an estimated 12,000 millionaires among Microsoft employees. Since the 1990s, it has increasingly diversified its business. Steve Ballmer replaced Gates as CEO in 2000. He oversaw the then-largest of Microsoft's corporate acquisitions in Skype Technologies in 2011, an increased focus on hardware that led to its first in-house PC line—the Surface—in 2012, and the formation of Microsoft Mobile through Nokia. Since Satya Nadella became CEO in 2014, the company has changed focus towards cloud computing and acquired LinkedIn in 2016. Under his direction, the company has expanded its video gaming business to support the Xbox brand, establishing the Microsoft Gaming division in 2022 and acquiring Activision Blizzard in 2023.

Microsoft has been dominant in the IBM PC–compatible operating system and office software suite markets since the 1990s. Its best-known software products are the Windows line of operating systems and the Microsoft Office and Microsoft 365 suite of productivity applications, which most notably include the Word word processor, Excel spreadsheet editor, and PowerPoint presentation program. Its flagship hardware products are the Surface lineup of PCs and the Xbox brand of video game consoles, the latter including the Xbox network. The company also provides a range of consumer Internet services such as Bing web search, the MSN web portal, the Outlook.com (Hotmail) email service, and the Microsoft Store. In the enterprise and development fields, Microsoft most notably provides the Azure cloud computing platform, Microsoft SQL Server database software, and Visual Studio.

Microsoft became the third publicly traded U.S. company to be valued at over $1 trillion in April 2019. It has been criticized for monopolistic practices, and the company's software received criticism for problems with ease of use, robustness, and security. Microsoft has also been criticized for its role in providing services to Israel during the Gaza war.
    """

    summary_template="""
    given the information {information} about a company I want you to create:
    1. A short summary
    2. two interesting facts about it
    """

    summary_prompt_template=PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(temperature=0, model="gpt-5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response= chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
