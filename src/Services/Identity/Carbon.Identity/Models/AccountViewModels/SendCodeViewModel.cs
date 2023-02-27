using Microsoft.AspNetCore.Mvc.Rendering;

namespace Carbon.Identity.Models.AccountViewModels;
public record SendCodeViewModel
{
    public required string SelectedProvider { get; init; }

    public required ICollection<SelectListItem> Providers { get; init; }

    public required string ReturnUrl { get; init; }

    public bool RememberMe { get; init; }
}
