namespace Carbon.Identity.Services;
public interface IRedirectService
{
    string ExtractRedirectUriFromReturnUrl(string url);
}