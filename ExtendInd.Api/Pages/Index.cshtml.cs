using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;


namespace ExtendInd.Api.Pages;

public class IndexModel : PageModel
{
    private readonly ILogger<IndexModel> _logger;

    public IndexModel(ILogger<IndexModel> logger)
    {
        _logger = logger;
    }

    public void OnGet(string? page = null)
    {
        if (!string.IsNullOrEmpty(page))
        {
            ViewData["PageToLoad"] = page; // Defines which partial will be loaded
        }
        else
        {
            ViewData["PageToLoad"] = "_Index"; // Load page About by default
        }
    }
}
