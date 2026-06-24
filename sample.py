"""
Sample usage examples for the LangChain AI Project.

This file demonstrates various ways to use the LangChain project
with different companies, prompts, and LLM configurations.
"""

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def get_llm(provider="ollama"):
    """
    Get the appropriate LLM instance based on provider.
    
    Args:
        provider (str): "openai" or "ollama" (default)
    
    Returns:
        ChatOpenAI or ChatOllama instance
    """
    if provider.lower() == "openai":
        return ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    else:
        return ChatOllama(temperature=0, model="gemma3:270m")


def example_1_basic_summary():
    """Example 1: Generate a basic summary of a company."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Company Summary")
    print("="*60 + "\n")
    
    company_info = """
    Apple Inc. is an American multinational technology company headquartered in Cupertino, California.
    Apple is the largest technology company by revenue, with annual revenue exceeding $380 billion.
    The company is known for its iPhone, iPad, Mac computers, and services like Apple Music and iCloud.
    Founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne, Apple has become one of the
    world's most valuable companies with a market capitalization exceeding $3 trillion.
    """
    
    template = """
    Given the following information about a company, provide:
    1. A concise summary (2-3 sentences)
    2. Two interesting facts
    3. Key strengths
    
    Company Information: {information}
    """
    
    prompt = PromptTemplate(input_variables=["information"], template=template)
    
    llm = get_llm("ollama")  # Using local Ollama
    chain = prompt | llm
    
    response = chain.invoke(input={"information": company_info})
    print(response.content)


def example_2_detailed_analysis():
    """Example 2: Detailed company analysis."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Detailed Company Analysis")
    print("="*60 + "\n")
    
    company_info = """
    Google LLC is an American multinational technology company that specializes in 
    Internet-related services and products. Google operates the world's largest search engine
    and offers a suite of products including Gmail, Google Drive, Google Maps, YouTube, and Android OS.
    The company was founded in 1998 by Larry Page and Sergey Brin and is now owned by parent 
    company Alphabet Inc., established in 2015.
    """
    
    template = """
    Analyze the following company and provide:
    1. Company Overview (1-2 sentences)
    2. Main Products/Services (list 3-5 key products)
    3. Market Position
    4. Innovation Areas
    
    Company Information: {information}
    """
    
    prompt = PromptTemplate(input_variables=["information"], template=template)
    
    llm = get_llm("ollama")
    chain = prompt | llm
    
    response = chain.invoke(input={"information": company_info})
    print(response.content)


def example_3_custom_prompt():
    """Example 3: Custom prompt for industry analysis."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Industry Analysis")
    print("="*60 + "\n")
    
    company_info = """
    Tesla, Inc. is an American automotive and energy storage company.
    The company specializes in electric vehicles (EVs), battery storage systems, and solar panels.
    Founded in 2003 by Martin Eberhard and Marc Tarpenning, Tesla is led by CEO Elon Musk.
    Tesla operates Gigafactories in multiple countries and has delivered over 5 million vehicles.
    The company is at the forefront of the EV revolution and sustainable energy adoption.
    """
    
    template = """
    Based on the company description below, provide insights on:
    1. Industry Impact: How is this company impacting its industry?
    2. Competitive Advantages: What makes this company stand out?
    3. Future Potential: What opportunities lie ahead?
    4. Challenges: What challenges might the company face?
    
    Company Information: {information}
    """
    
    prompt = PromptTemplate(input_variables=["information"], template=template)
    
    llm = get_llm("ollama")
    chain = prompt | llm
    
    response = chain.invoke(input={"information": company_info})
    print(response.content)


def example_4_batch_processing():
    """Example 4: Batch processing multiple companies."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Batch Processing Multiple Companies")
    print("="*60 + "\n")
    
    companies = [
        {
            "name": "Amazon",
            "info": """Amazon.com, Inc. is an American multinational e-commerce and cloud computing company.
            The company operates Amazon.com, the world's largest online retailer, and Amazon Web Services (AWS),
            a leading cloud computing platform. Founded in 1994 by Jeff Bezos, Amazon has expanded to offer
            streaming services, digital assistants, and grocery delivery."""
        },
        {
            "name": "Meta",
            "info": """Meta Platforms, Inc. (formerly Facebook) is an American technology company that builds
            products to help people connect. The company operates Facebook, Instagram, WhatsApp, and is investing
            heavily in the metaverse. Founded in 2004 by Mark Zuckerberg, Meta has over 3 billion monthly users
            across its platforms."""
        }
    ]
    
    template = """
    Given this company information, provide a 2-3 sentence summary and one key insight.
    
    Company: {name}
    Information: {info}
    """
    
    prompt = PromptTemplate(input_variables=["name", "info"], template=template)
    
    llm = get_llm("ollama")
    chain = prompt | llm
    
    for company in companies:
        print(f"\n>>> Processing {company['name']}...")
        response = chain.invoke(input={"name": company["name"], "info": company["info"]})
        print(response.content)


def example_5_temperature_comparison():
    """Example 5: Comparing different temperature settings."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Temperature Settings Comparison")
    print("="*60 + "\n")
    
    company_info = """
    Netflix, Inc. is a streaming media and video rental service company.
    Founded in 1997 by Reed Hastings and Marc Randolph, Netflix offers a vast library of
    TV shows, movies, and original content. The company pioneered the subscription streaming model
    and operates in over 190 countries with millions of subscribers.
    """
    
    template = """
    Create a creative marketing tagline for this company based on its description.
    
    Company Information: {information}
    """
    
    prompt = PromptTemplate(input_variables=["information"], template=template)
    
    temperatures = [0, 0.5, 1.0]
    
    for temp in temperatures:
        print(f"\n--- Temperature: {temp} ---")
        llm = ChatOllama(temperature=temp, model="gemma3:270m")
        chain = prompt | llm
        response = chain.invoke(input={"information": company_info})
        print(response.content)


def example_6_error_handling():
    """Example 6: Error handling and graceful fallbacks."""
    print("\n" + "="*60)
    print("EXAMPLE 6: Error Handling")
    print("="*60 + "\n")
    
    company_info = """
    IBM (International Business Machines Corporation) is a multinational technology company
    providing hardware, software, and IT services. Founded in 1911, IBM has evolved from
    manufacturing typewriters to becoming a leader in computing and AI solutions.
    """
    
    template = """
    Summarize this company: {information}
    """
    
    prompt = PromptTemplate(input_variables=["information"], template=template)
    
    try:
        # Try with Ollama first
        llm = get_llm("ollama")
        chain = prompt | llm
        response = chain.invoke(input={"information": company_info})
        print("✓ Successfully processed with Ollama")
        print(response.content)
    except Exception as e:
        print(f"✗ Ollama failed: {str(e)}")
        print("Attempting fallback to OpenAI...")
        try:
            llm = get_llm("openai")
            chain = prompt | llm
            response = chain.invoke(input={"information": company_info})
            print("✓ Successfully processed with OpenAI")
            print(response.content)
        except Exception as e2:
            print(f"✗ OpenAI also failed: {str(e2)}")


def main():
    """Run all examples."""
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  LangChain AI Project - Sample Examples".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    try:
        # Run examples
        example_1_basic_summary()
        example_2_detailed_analysis()
        example_3_custom_prompt()
        example_4_batch_processing()
        # example_5_temperature_comparison()  # Uncomment to compare temperatures
        # example_6_error_handling()  # Uncomment to test error handling
        
        print("\n" + "="*60)
        print("All examples completed!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error running examples: {str(e)}")
        print("Make sure Ollama is running or OpenAI API key is configured.")


if __name__ == "__main__":
    main()
