using Carbon.Identity.Data;
using Duende.IdentityServer.EntityFramework.Options;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace Carbon.Identity.Factories;

public class ConfigurationDbContextFactory : IDesignTimeDbContextFactory<ConfigurationDbContext>
{
    public ConfigurationDbContext CreateDbContext(string[] args)
    {
        string environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT");

        var config = new Microsoft.Extensions.Configuration.ConfigurationBuilder()
            .SetBasePath(Path.Combine(Directory.GetCurrentDirectory()))
            .AddJsonFile("appsettings.json")
            .AddJsonFile($"appsettings.{environment}.json", optional: true)
            .AddEnvironmentVariables()
            .Build();

        var optionsBuilder = new DbContextOptionsBuilder<ConfigurationDbContext>();
        var storeOptions = new ConfigurationStoreOptions();
        optionsBuilder.UseNpgsql(config["ConnectionStrings:DefaultConnection"], npgsqlOptionsAction: o => o.MigrationsAssembly("Carbon.Identity"));

        var dbContext = new ConfigurationDbContext(optionsBuilder.Options);
        dbContext.StoreOptions = storeOptions;

        return dbContext;
        //return new ConfigurationDbContext(optionsBuilder.Options);
    }
}