using Carbon.Identity.Data;
using Duende.IdentityServer.EntityFramework.Options;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace Carbon.Identity.Factories;

public class PersistedGrantDbContextFactory : IDesignTimeDbContextFactory<PersistedGrantDbContext>
{
    public PersistedGrantDbContext CreateDbContext(string[] args)
    {
        string environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT");

        var config = new Microsoft.Extensions.Configuration.ConfigurationBuilder()
            .SetBasePath(Path.Combine(Directory.GetCurrentDirectory()))
            .AddJsonFile("appsettings.json")
            .AddJsonFile($"appsettings.{environment}.json", optional: true)
            .AddEnvironmentVariables()
            .Build();

        var optionsBuilder = new DbContextOptionsBuilder<PersistedGrantDbContext>();
        var operationOptions = new OperationalStoreOptions();

        optionsBuilder.UseNpgsql(config["ConnectionStrings:DefaultConnection"], npgsqlOptionsAction: o => o.MigrationsAssembly("Carbon.Identity"));

        var dbContext = new PersistedGrantDbContext(optionsBuilder.Options);
        dbContext.StoreOptions = operationOptions;

        return dbContext;
        // return new PersistedGrantDbContext(optionsBuilder.Options);
    }
}
